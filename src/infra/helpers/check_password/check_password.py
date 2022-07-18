from src.data.interfaces import CheckPassword
from werkzeug.security import check_password_hash


class CheckPassword(CheckPassword):
    def check(self, password_hash: str, password: str) -> bool:
        return check_password_hash(password_hash, password)
