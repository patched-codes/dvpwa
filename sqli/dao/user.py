from typing import NamedTuple, Optional, Tuple
import base64
import os
from hashlib import md5
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

from aiopg import Connection


class User:
    def __init__(self, id: int, first_name: str, middle_name: Optional[str], 
                 last_name: str, username: str, pwd_hash: str, is_admin: bool):
        self.id = id
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.username = username
        self.pwd_hash = pwd_hash
        self.is_admin = is_admin

    @classmethod
    def from_raw(cls, raw: tuple):
        return cls(*raw) if raw else None

    @staticmethod
    async def get(conn: Connection, id_: int):
        async with conn.cursor() as cur:
            await cur.execute(
                'SELECT id, first_name, middle_name, last_name, '
                'username, pwd_hash, is_admin FROM users WHERE id = %s',
                (id_,),
            )
            return User.from_raw(await cur.fetchone())

    @staticmethod
    async def get_by_username(conn: Connection, username: str):
        async with conn.cursor() as cur:
            await cur.execute(
                'SELECT id, first_name, middle_name, last_name, '
                'username, pwd_hash, is_admin FROM users WHERE username = %s',
                (username,),
            )
            return User.from_raw(await cur.fetchone())

    @staticmethod
    def _is_legacy_hash(pwd_hash: str) -> bool:
        """Check if hash is a legacy MD5 hash (32 hex chars)"""
        return len(pwd_hash) == 32 and all(c in '0123456789abcdef' for c in pwd_hash.lower())

    @staticmethod
    def _check_legacy_password(stored_hash: str, password: str) -> bool:
        """Verify password against legacy MD5 hash"""
        password_hash = md5(password.encode('utf-8')).hexdigest()
        return stored_hash.lower() == password_hash.lower()

    @staticmethod
    def _generate_new_hash(password: str) -> str:
        """Generate a new secure hash using PBKDF2-SHA256"""
        salt = os.urandom(16)
        # Using PBKDF2 with SHA256, 600000 iterations
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=600000,
        )
        key = kdf.derive(password.encode('utf-8'))
        
        # Format: v2$salt_b64$hash_b64
        salt_b64 = base64.b64encode(salt).decode('utf-8')
        hash_b64 = base64.b64encode(key).decode('utf-8')
        return f"v2${salt_b64}${hash_b64}"

    @staticmethod
    def _verify_current_hash(stored_hash: str, password: str) -> bool:
        """Verify password against current version hash"""
        try:
            # Parse hash components
            version, salt_b64, hash_b64 = stored_hash.split('$')
            if version != 'v2':
                return False

            salt = base64.b64decode(salt_b64)
            stored_key = base64.b64decode(hash_b64)
            
            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,
                salt=salt,
                iterations=600000,
            )
            
            test_key = kdf.derive(password.encode('utf-8'))
            return test_key == stored_key
            
        except Exception:
            return False

    def check_password(self, password: str) -> Tuple[bool, Optional[str]]:
        """
        Check if password matches stored hash.
        Returns (is_valid, new_hash) where new_hash is provided if password
        was correct but needs upgrading from legacy format
        """
        if self._is_legacy_hash(self.pwd_hash):
            # Handle legacy MD5 hash
            is_valid = self._check_legacy_password(self.pwd_hash, password)
            if is_valid:
                # If valid, return new secure hash for upgrading
                return True, self._generate_new_hash(password)
            return False, None
            
        # Handle current version hash
        is_valid = self._verify_current_hash(self.pwd_hash, password)
        return is_valid, None

    @classmethod
    def hash_new_password(cls, password: str) -> str:
        """Generate hash for a new password using current secure method"""
        return cls._generate_new_hash(password)
