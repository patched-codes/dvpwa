from typing import NamedTuple, Optional, Tuple

from aiopg import Connection
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import os
import base64


class User(NamedTuple):
    id: int
    first_name: str
    middle_name: Optional[str]
    last_name: str
    username: str
    pwd_hash: str
    pwd_salt: str  # New field for password salt
    is_admin: bool

    @classmethod
    def from_raw(cls, raw: tuple):
        return cls(*raw) if raw else None

    @staticmethod
    async def get(conn: Connection, id_: int):
        async with conn.cursor() as cur:
            await cur.execute(
                'SELECT id, first_name, middle_name, last_name, '
                'username, pwd_hash, pwd_salt, is_admin FROM users WHERE id = %s',
                (id_,),
            )
            return User.from_raw(await cur.fetchone())

    @staticmethod
    async def get_by_username(conn: Connection, username: str):
        async with conn.cursor() as cur:
            await cur.execute(
                'SELECT id, first_name, middle_name, last_name, '
                'username, pwd_hash, pwd_salt, is_admin FROM users WHERE username = %s',
                (username,),
            )
            return User.from_raw(await cur.fetchone())

    @staticmethod
    def hash_password(password: str) -> Tuple[str, str]:
        """Hash a password using PBKDF2 with SHA256.
        
        Returns:
            Tuple containing (password_hash, salt) both base64 encoded
        """
        salt = os.urandom(16)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        pwd_hash = base64.b64encode(kdf.derive(password.encode('utf-8'))).decode('utf-8')
        pwd_salt = base64.b64encode(salt).decode('utf-8')
        return pwd_hash, pwd_salt

    def check_password(self, password: str) -> bool:
        """Verify a password against the stored hash using PBKDF2.
        
        Args:
            password: The password to verify

        Returns:
            bool: True if password matches, False otherwise
        """
        try:
            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,
                salt=base64.b64decode(self.pwd_salt),
                iterations=100000,
                backend=default_backend()
            )
            test_hash = base64.b64encode(kdf.derive(password.encode('utf-8'))).decode('utf-8')
            return self.pwd_hash == test_hash
        except Exception:
            return False
