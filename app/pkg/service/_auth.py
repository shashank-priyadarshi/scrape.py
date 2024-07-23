import random
import string
from datetime import datetime, timedelta
from typing import Optional

import jwt

from ..abstract.database import Database
from ..logger.logger import LoggerSingleton

key = "your-secret-key"  # Replace with your actual secret key
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


class _Auth:
    def __init__(self, logger: LoggerSingleton, db: Database):
        self.logger = logger
        self.database = db

    def verify_jwt(self, token: str) -> Optional[dict]:
        try:
            payload = jwt.decode(token, key, algorithms=[ALGORITHM])
            return payload
        except jwt.ExpiredSignatureError:
            self.logger.warning("Token has expired.")
            return None
        except jwt.InvalidTokenError:
            self.logger.warning("Invalid token.")
            return None

    def create_jwt(self, claims: Optional[dict] = None) -> str:
        if claims is None:
            claims = {
                "sub": ''.join(random.choices(string.ascii_letters + string.digits, k=10)),
                "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
            }
        token = jwt.encode(claims, key, algorithm=ALGORITHM)
        return token


def _new(logger: LoggerSingleton, db: Database) -> _Auth:
    return _Auth(logger, db)
