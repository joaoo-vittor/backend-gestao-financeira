from src.data.interfaces import Encrypter
from werkzeug.security import generate_password_hash


class Encrypter(Encrypter):
    def encrypt(self, value: str) -> str:
        return generate_password_hash(password=value)
