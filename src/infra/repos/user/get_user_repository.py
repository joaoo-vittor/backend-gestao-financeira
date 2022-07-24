from typing import Union
from src.data.interfaces.repository import GetUserRepositoryInterface
from src.domain.models.user import UserData, GetUserParams, PlanContract, Plan
from src.infra.config import DBConnectionHandler
from src.infra.entities import UserModel


class GetUserRepository(GetUserRepositoryInterface):
    def __init__(self, connection_handler: DBConnectionHandler) -> None:
        self.__connection_handler = connection_handler

    def find_user_by(self, user_params: GetUserParams) -> Union[UserData, None]:
        """Find user by id and email

        Args:
            user_params (GetUserParams): data with id and email of the user

        Returns:
            Union[UserData, None]: data of the user
        """

        if user_params is None:
            return None

        try:
            session = self.__connection_handler.get_session()

            user_data = (
                session.query(UserModel)
                .filter_by(id=user_params["id"], email=user_params["email"])
                .one_or_none()
            )

            if user_data is None:
                return None

            user_plan_contract = [
                PlanContract(
                    user_id=p.user_id,
                    plan_id=p.plan_id,
                    value_plan=p.value_plan,
                    start_time_stamp=str(p.start_time_stamp),
                    end_time_stamp=str(p.end_time_stamp),
                    active=p.active,
                    plan=Plan(type=p.plan.type, active=p.plan.active),
                )
                for p in user_data.plan_contract
            ]

            return UserData(
                id=user_data.id,
                name=user_data.name,
                email=user_data.email,
                plan_contract=user_plan_contract,
            )

        except Exception:
            session.rollback()
            raise

        finally:
            session.close()
