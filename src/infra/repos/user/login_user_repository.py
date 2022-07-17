from typing import Union
from src.data.interfaces import FindUserRespositoryInterface
from src.domain.models.user import UserModel as User
from src.domain.usecases.user import FindUserModel
from src.infra.entities import User as UserModel
from src.infra.config import DBConnectionHandler


class LoginUserRepository(FindUserRespositoryInterface):
    def __init__(self, connection_handler: DBConnectionHandler) -> None:
        self.__connection_handler = connection_handler

    def find_user(self, user_data: FindUserModel) -> Union[UserModel, None]:
        """Login user

        Args:
            user_data (FindUserModel): model with data to find user

        Returns:
            UserModel: model with data of the user to login
        """

        if user_data is None:
            return None

        try:
            session = self.__connection_handler.get_session()
            user = (
                session.query(UserModel)
                .filter_by(email=user_data["email"])
                .one_or_none()
            )

            if user is None:
                return None

            return User(
                name=user.name, email=user.email, password_hash=user.password_hash
            )

        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
