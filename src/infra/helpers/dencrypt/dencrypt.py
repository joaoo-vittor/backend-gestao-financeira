from datetime import datetime, timezone
from src.presentation.interface import Decrypt
from flask_jwt_extended import decode_token


class DecryptToken(Decrypt):
    def dencrypt(self, token: str) -> dict:
        data_token = decode_token(token)
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now)
        if target_timestamp > data_token["exp"]:
            return {}
        return data_token["sub"]
