from typing import Any, Union
from src.domain.models.user import UserLogin, Plan, PlanContract
from faker import Faker

faker = Faker()


class LoginUserRepositorySpy:
    def __init__(self, connection_handler: Any) -> None:
        self.__connection_handler = connection_handler
        self.user_data = None

    def find_user(self, user_data: Any) -> Union[UserLogin, None]:
        self.user_data = user_data

        user_id = faker.random_digit_not_null()
        plan = Plan(type="Freemium", active=True)
        plan_contract = PlanContract(
            user_id=user_id,
            plan_id=faker.random_digit_not_null(),
            value_plan=faker.random_number(digits=3),
            start_time_stamp=faker.date(),
            end_time_stamp=faker.date(),
            active=True,
        )

        return UserLogin(
            id=user_id,
            email=user_data["email"],
            password_hash=user_data["password"],
            plan_contract=plan_contract,
            plan=plan,
        )
