from typing import Union
from src.data.interfaces import FindUserRespositoryInterface
from src.domain.models.user import UserLogin, PlanContract, Plan
from src.domain.usecases.user import LoginUserModel
from src.infra.entities import UserModel, PlansContractModel, PlanModel
from src.infra.config import DBConnectionHandler


class LoginUserRepository(FindUserRespositoryInterface):
    def __init__(self, connection_handler: DBConnectionHandler) -> None:
        self.__connection_handler = connection_handler

    def find_user(self, user_data: LoginUserModel) -> Union[UserLogin, None]:
        """Login user

        Args:
            user_data (LoginUserModel): model with data to find user

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
                .join(PlansContractModel, UserModel.id == PlansContractModel.user_id)
                .join(PlanModel, PlanModel.id == PlansContractModel.plan_id)
                .one_or_none()
            )

            if user is None:
                return None

            user_plan_contract = [
                PlanContract(
                    user_id=p.user_id,
                    plan_id=p.plan_id,
                    value_plan=p.value_plan,
                    start_time_stamp=p.start_time_stamp,
                    end_time_stamp=p.end_time_stamp,
                    active=p.active,
                )
                for p in user.plan_contract
            ]

            plan = [
                Plan(type=p.plan.type, active=p.plan.active) for p in user.plan_contract
            ]

            return UserLogin(
                name=user.name,
                email=user.email,
                password_hash=user.password_hash,
                plan_contract=user_plan_contract,
                plan=plan,
            )

        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
