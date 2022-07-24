from typing import Any, Union
from faker import Faker

from src.domain.models.user import PlanContract, Plan, UserData

faker = Faker()


class GetUserUseCaseSpy:
    def __init__(self, get_user_repository: Any) -> None:
        self.__get_user_repository = get_user_repository
        self.user = None

    def get_user(self, user: Any) -> Union[Any, None]:
        """Use case to get user

        Args:
            user (GetUserParams): user data to get

        Returns:
            Union[UserData, None]: getted user data
        """

        if user is None:
            return None

        self.user = user

        plan_contract = PlanContract(
            user_id=user["id"],
            plan_id=faker.random_digit_not_null(),
            value_plan=faker.random_number(digits=3),
            start_time_stamp=faker.date(),
            end_time_stamp=faker.date(),
            active=True,
            plan=Plan(type="Freemium", active=True),
        )

        return UserData(
            id=user["id"],
            email=user["email"],
            plan_contract=plan_contract,
        )
