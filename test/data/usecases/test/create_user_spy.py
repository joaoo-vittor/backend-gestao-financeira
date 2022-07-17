from typing import Any
from src.domain.models.user import User


class CreateUserUseCaseSpy:
    def __init__(self, create_user_repository: Any, encrypter: Any) -> None:
        self.__encrypter = encrypter
        self.__create_user_repository = create_user_repository
        self.user = None

    def add(self, user: Any) -> Any:
        self.user = user
        return User(
            name=user["name"] if "name" in user.keys() else None, email=user["email"]
        )
