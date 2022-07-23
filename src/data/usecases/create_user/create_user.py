from typing import Union
from src.domain.usecases.user import CreateUserInterface, CreateUserModel
from src.domain.models.user import User
from src.data.interfaces.repository import (
    CreateUserRespositoryInterface as CreateUserRespository,
)
from src.data.interfaces import (
    Encrypter,
)


class CreateUserUseCase(CreateUserInterface):
    def __init__(
        self, create_user_repository: CreateUserRespository, encrypter: Encrypter
    ) -> None:
        self.__encrypter = encrypter
        self.__create_user_repository = create_user_repository

    def add(self, user: CreateUserModel) -> Union[User, None]:
        """Add user

        Args:
            user (CreateUserModel): model with data to create user

        Returns:
            UserModel: model with data of user created
        """

        if user is None:
            return None

        password_hashed = self.__encrypter.encrypt(user["password"])
        user["password"] = password_hashed

        response = self.__create_user_repository.create_user(user)

        return response
