from dataclasses import dataclass
from src.presentation.interface import Validator
from src.presentation.controllers.login_user import LoginUserController
from test.data.usecases.test import LoginUserUseCaseSpy
from test.infra.repos.test import LoginUserRepositorySpy
from src.presentation.helpers.http import HttpRequest


class ValidateBodyLoginUser(Validator):
    def __init__(self) -> None:
        self.is_valid = True

    def validate(self, data: dict) -> bool:
        return self.is_valid


@dataclass
class SutTypes:
    sut: LoginUserController
    validator: ValidateBodyLoginUser


def make_sut() -> SutTypes:
    repo = LoginUserRepositorySpy(None)
    usecase = LoginUserUseCaseSpy(repo, None, None)
    validator = ValidateBodyLoginUser()
    sut = LoginUserController(usecase, validator)
    return SutTypes(sut=sut, validator=validator)


class ValidateBodyLoginUserWithRaise(Validator):
    def validate(self, data: dict) -> bool:
        raise Exception("")


def make_sut_with_exception() -> SutTypes:
    repo = LoginUserRepositorySpy(None)
    usecase = LoginUserUseCaseSpy(repo, None, None)
    validator = ValidateBodyLoginUserWithRaise()
    sut = LoginUserController(usecase, validator)
    return SutTypes(sut=sut, validator=validator)


def test_should_return_status_200_if_http_request_is_valid():
    data_sut = make_sut()
    sut = data_sut.sut

    http_request = HttpRequest(
        body={"email": "any_email@email.com", "password": "any_password"}
    )

    http_response = sut.handler(http_request)

    assert http_response.status_code == 200
    assert http_response.body["data"]["type"] == "auth"
    assert "authentication" in http_response.body["data"]["tokens"].keys()
    assert "authorization" in http_response.body["data"]["tokens"].keys()


def test_should_return_status_400_if_http_request_is_invalid():
    data_sut = make_sut()
    sut = data_sut.sut

    http_response = sut.handler(None)

    assert http_response.status_code == 400
    assert "error" in http_response.body["errors"]["body"].keys()


def test_should_return_status_422_if_body_is_invalid():
    data_sut = make_sut()
    sut = data_sut.sut
    validator = data_sut.validator

    http_request = HttpRequest(
        body={"email": "any_email@email.com", "password": "any_password"}
    )

    validator.is_valid = False
    http_response = sut.handler(http_request)

    assert http_response.status_code == 422
    assert "error" in http_response.body["errors"]["body"].keys()


def test_should_return_status_500_if_raise_exception():
    sut = make_sut_with_exception().sut

    http_request = HttpRequest(
        body={"email": "any_email@email.com", "password": "any_password"}
    )

    http_response = sut.handler(http_request)

    assert http_response.status_code == 500
    assert "error" in http_response.body["errors"]["body"].keys()
