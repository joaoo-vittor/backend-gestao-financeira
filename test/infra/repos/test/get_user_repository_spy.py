from typing import Any, Union
from src.domain.models.user import UserData, Plan, PlanContract
from faker import Faker

faker = Faker()


class GetUserRepositorySpy:
    def __init__(self, connection_handler) -> None:
        self.__connection_handler = connection_handler
        self.user_data = None

    def find_user_by(self, user_data: dict) -> Union[Any, None]:
        """Get user

        Args:
            user_data (GetUserModel): model with data to Get user

        Returns:
            UserModel: model with data of the user
        """

        if user_data is None:
            return None

        self.user_data = user_data

        plan_contract = PlanContract(
            user_id=user_data["id"],
            plan_id=faker.random_digit_not_null(),
            value_plan=faker.random_number(digits=3),
            start_time_stamp=faker.date(),
            end_time_stamp=faker.date(),
            active=True,
            plan=Plan(type="Freemium", active=True),
        )

        return UserData(
            id=user_data["id"],
            email=user_data["email"],
            plan_contract=plan_contract,
        )
