from hashlib import scrypt
from typing import NamedTuple, Optional

from aiopg import Connection


class User(NamedTuple):
    # ...same code...

    def check_password(self, password: str):
        return scrypt(password.encode('utf-8')).encode(hex=True) == self.pwd_hash
