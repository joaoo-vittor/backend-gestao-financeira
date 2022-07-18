import datetime
from src.data.interfaces import GenerateToken
from flask_jwt_extended import create_access_token


class GenerateToken(GenerateToken):
    def generate_token(self, payload: dict) -> str:
        return create_access_token(
            identity=payload,
            expires_delta=datetime.timedelta(days=7),
        )
