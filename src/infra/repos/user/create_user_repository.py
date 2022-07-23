import datetime
from typing import Union
from src.data.interfaces.repository import CreateUserRespositoryInterface
from src.domain.models.user import User
from src.infra.entities import UserModel, PlansContractModel
from src.domain.usecases.user import CreateUserModel
from src.infra.config import DBConnectionHandler


class CreateUserRepository(CreateUserRespositoryInterface):
    def __init__(self, connection_handler: DBConnectionHandler) -> None:
        self.__connection_handler = connection_handler

    def create_user(self, user_data: CreateUserModel) -> Union[User, None]:
        """Create user

        Args:
            user_data (CreateUserModel): model with data to create user

        Returns:
            UserModel: model with data of the user created
        """

        if user_data is None:
            return None

        if "name" in user_data.keys():
            user = UserModel(
                name=user_data["name"],
                email=user_data["email"],
                password_hash=user_data["password"],
            )
        else:
            user = UserModel(
                email=user_data["email"],
                password_hash=user_data["password"],
            )

        try:
            session = self.__connection_handler.get_session()
            session.add(user)

            data = (
                session.query(UserModel)
                .filter_by(email=user_data["email"])
                .one_or_none()
            )

            plan_contract = PlansContractModel(
                user_id=int(data.id),
                plan_id=1,
                value_plan=0.0,
                start_time_stamp=str(datetime.datetime.now()),
                end_time_stamp=str(
                    datetime.datetime.now() + datetime.timedelta(days=30)
                ),
                active=1,
            )

            session.add(plan_contract)
            session.commit()

            return User(
                name=user_data["name"] if "name" in user_data.keys() else None,
                email=user_data["email"],
            )

        except Exception:
            session.rollback()
            raise

        finally:
            session.close()
