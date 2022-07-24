from typing import Union
from src.domain.models.auth import Auth
from src.domain.usecases.user import LoginUserUseCaseInterface
from src.domain.usecases.user import LoginUserModel
from src.data.interfaces.repository import (
    LoginUserRespositoryInterface as LoginUserRespository,
)
from src.data.interfaces import (
    CheckPassword,
    GenerateToken,
)


class LoginUserUseCase(LoginUserUseCaseInterface):
    def __init__(
        self,
        login_user_repository: LoginUserRespository,
        check_password: CheckPassword,
        generate_token: GenerateToken,
    ) -> None:
        self.__login_user_repository = login_user_repository
        self.__check_password = check_password
        self.__generate_token = generate_token

    def auth(self, user: LoginUserModel) -> Union[Auth, None]:
        """authentication and authorization to user

        Args:
            user (LoginUserModel): data to make login

        Returns:
            Union[Auth, None]: access token and authorization token
        """

        if user is None:
            return None

        response = self.__login_user_repository.find_user(user)

        if response is None:
            return None

        password_is_valid = self.__check_password.check(
            response["password_hash"], user["password"]
        )

        if not password_is_valid:
            return None

        payload_authentication = {"id": response["id"], "email": response["email"]}
        payload_authorization = {
            "plan": {
                "name": response["plan_contract"]["plan"]["type"],
                "active": response["plan_contract"]["plan"]["active"],
            },
            "plan_contract": {
                "start_date": response["plan_contract"]["start_time_stamp"],
                "end_date": response["plan_contract"]["end_time_stamp"],
                "active": response["plan_contract"]["active"],
            },
        }

        tokens = Auth(
            authentication=self.__generate_token.generate_token(
                payload=payload_authentication
            ),
            authorization=self.__generate_token.generate_token(
                payload=payload_authorization
            ),
        )

        return tokens
