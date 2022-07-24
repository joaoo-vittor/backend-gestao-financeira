from typing import Type
from src.main.interface import HandlerInterface
from src.domain.usecases.user import GetUserUseCaseInterface as GetUserUseCase
from src.presentation.helpers.http import HttpRequest, HttpResponse
from src.presentation.interface import Validator, Decrypt
from src.presentation.errors import HttpErrors
from src.domain.models.user import GetUserParams


class GetUserController(HandlerInterface):
    def __init__(
        self,
        get_user_usecase: GetUserUseCase,
        validator: Validator,
        dencrypt: Decrypt,
    ) -> None:
        self.__get_user_usecase = get_user_usecase
        self.__validator = validator
        self.__dencrypt = dencrypt

    def handler(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Handler to call on route

        Args:
            http_request (Type[HttpRequest]): http request with data

        Returns:
            HttpResponse: response data
        """

        response = None

        if http_request is None or http_request.header is None:
            http_error = HttpErrors.error_400()
            return HttpResponse(
                status_code=http_error["errors"]["status_code"],
                body=http_error,
            )

        try:
            payload = self.__dencrypt.dencrypt(http_request.header["Authentication"])
            header_is_valid = self.__validator.validate(payload)

            if not header_is_valid:
                http_error = HttpErrors.error_401()
                return HttpResponse(
                    status_code=http_error["errors"]["status_code"],
                    body=http_error,
                )

            user = GetUserParams(**payload)
            response = self.__get_user_usecase.get_user(user)

            if response is None:
                http_error = HttpErrors.error_400()
                return HttpResponse(
                    status_code=http_error["errors"]["status_code"],
                    body=http_error,
                )

        except Exception as e:
            print(e)
            http_error = HttpErrors.error_500()
            return HttpResponse(
                status_code=http_error["errors"]["status_code"],
                body=http_error,
            )

        return HttpResponse(
            status_code=200,
            body={
                "data": {
                    "type": "user",
                    "user": response,
                }
            },
        )
