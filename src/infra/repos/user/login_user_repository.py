from typing import Union
from src.data.interfaces import FindUserRespositoryInterface
from src.domain.usecases.user import CreateUserModel
from src.infra.entities import User as UserModel
from src.infra.config import DBConnectionHandler


class LoginUserRepository(FindUserRespositoryInterface):
    def __init__(self, connection_handler: DBConnectionHandler) -> None:
        self.__connection_handler = connection_handler

    def find_user(self, user_data: CreateUserModel) -> Union[UserModel, None]:
        """Login user

        Args:
            user_data (CreateUserModel): model with data to find user

        Returns:
            UserModel: model with data of the user to login
        """

        if user_data is None:
            return None
