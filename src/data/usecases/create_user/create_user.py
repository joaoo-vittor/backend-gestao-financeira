from typing import Union
from src.domain.usecases import CreateUserInterface, CreateUserModel
from src.domain.models import UserModel
from src.data.interfaces import (
    Encrypter,
    CreateUserRespositoryInterface as CreateUserRespository,
)


class CreateUserUseCase(CreateUserInterface):
    def __init__(
        self, create_user_repository: CreateUserRespository, encrypter: Encrypter
    ) -> None:
        self.__encrypter = encrypter
        self.__create_user_repository = create_user_repository

    def add(self, user: CreateUserModel) -> Union[UserModel, None]:
        """Add user

        Args:
            user (CreateUserModel): model with data to create user

        Returns:
            UserModel: model with data of user created
        """

        password_hashed = self.__encrypter.encrypt(user["password"])
        user["password"] = password_hashed

        response = self.__create_user_repository.create_user(user)

        if response:
            return response

        return None