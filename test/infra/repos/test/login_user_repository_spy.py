from typing import Any, Union
from src.domain.models.user import User


class LoginUserRepository:
    def __init__(self, connection_handler: Any) -> None:
        self.__connection_handler = connection_handler
        self.user_data = None

    def find_user(self, user_data: Any) -> Union[User, None]:
        self.user_data = user_data

        return User(email=user_data["email"], password_hash=user_data["password"])
