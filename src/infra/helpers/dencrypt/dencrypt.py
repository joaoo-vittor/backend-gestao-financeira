from src.presentation.interface import Decrypt
from flask_jwt_extended import decode_token


class DecryptToken(Decrypt):
    def dencrypt(self, token: str) -> dict:
        return decode_token(token)
