from typing import Any


class LoginUserUseCaseSpy:
    def __init__(
        self,
        login_user_repository: Any,
        check_password: Any,
        generate_token: Any,
    ) -> None:
        self.__login_user_repository = login_user_repository
        self.__check_password = check_password
        self.__generate_token = generate_token
        self.user = None
        self.is_valid = True

    def auth(self, user: Any) -> Any:
        self.user = user
        tokens = {
            "authentication": "any_token",
            "authorization": "any_token",
        }
        return tokens if self.is_valid else None
