from typing import Type
from src.main.interface import HandlerInterface
from src.domain.usecases.user import LoginUserUseCaseInterface as LoginUserUseCase
from src.presentation.helpers.http import HttpRequest, HttpResponse
from src.presentation.interface import Validator
from src.presentation.errors import HttpErrors
from src.domain.usecases.user import LoginUserModel


class LoginUserController(HandlerInterface):
    def __init__(
        self, login_user_usecase: LoginUserUseCase, validator: Validator
    ) -> None:
        self.__login_user_usecase = login_user_usecase
        self.__validator = validator

    def handler(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Handler to call on route

        Args:
            http_request (Type[HttpRequest]): http request with data

        Returns:
            HttpResponse: response data
        """

        response = None

        if http_request is not None and http_request.body:
            try:
                body_is_valid = self.__validator.validate(http_request.body)

                if body_is_valid:
                    user = LoginUserModel(**http_request.body)
                    response = self.__login_user_usecase.auth(user)
                    return HttpResponse(
                        status_code=200,
                        body={
                            "data": {
                                "type": "auth",
                                "tokens": response,
                            }
                        },
                    )

                http_error = HttpErrors.error_422()
                return HttpResponse(
                    status_code=http_error["errors"]["status_code"],
                    body=http_error,
                )

            except Exception:
                http_error = HttpErrors.error_500()
                return HttpResponse(
                    status_code=http_error["errors"]["status_code"],
                    body=http_error,
                )

        http_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=http_error["errors"]["status_code"],
            body=http_error,
        )
