from typing import Union
from src.domain.models.user import UserData, GetUserParams
from src.domain.usecases.user import GetUserUseCaseInterface
from src.data.interfaces.repository import (
    GetUserRepositoryInterface as GetUserRepository,
)


class GetUserUseCase(GetUserUseCaseInterface):
    def __init__(self, get_user_repository: GetUserRepository) -> None:
        self.__get_user_repository = get_user_repository

    def get_user(self, user: GetUserParams) -> Union[UserData, None]:
        """Use case to get user

        Args:
            user (GetUserParams): user data to get

        Returns:
            Union[UserData, None]: getted user data
        """

        if user is None:
            return None

        user_data = self.__get_user_repository.find_user_by(user)

        return user_data
