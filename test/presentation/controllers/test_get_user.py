from dataclasses import dataclass
from faker import Faker
from src.presentation.interface import Validator, Decrypt
from src.presentation.controllers.get_user import GetUserController
from test.data.usecases.test import GetUserUseCaseSpy
from test.infra.repos.test import GetUserRepositorySpy
from src.presentation.helpers.http import HttpRequest

faker = Faker()


class ValidateHeaderGetUserSpy(Validator):
    def __init__(self) -> None:
        self.is_valid = True

    def validate(self, data: dict) -> bool:
        return self.is_valid


class DecryptSpy(Decrypt):
    def __init__(self) -> None:
        self.payload = {"id": faker.random_number(), "email": faker.email()}

    def dencrypt(self, token: str) -> dict:
        return self.payload


@dataclass
class SutTypes:
    validator: ValidateHeaderGetUserSpy
    decrypt: DecryptSpy
    sut: GetUserController


def make_sut() -> SutTypes:
    repo = GetUserRepositorySpy(None)
    use_case = GetUserUseCaseSpy(repo)
    validator = ValidateHeaderGetUserSpy()
    decrypt = DecryptSpy()
    sut = GetUserController(use_case, validator, decrypt)
    return SutTypes(sut=sut, validator=validator, decrypt=decrypt)


def test_should_return_user_if_authentication_token_in_header_is_valid():
    data_sut = make_sut()
    sut = data_sut.sut
    decrypt = data_sut.decrypt

    header = {"Authentication": "any_token"}
    http_request = HttpRequest(header=header)

    response = sut.handler(http_request)

    assert response.status_code == 200
    assert response.body["data"]["user"]["id"] == decrypt.payload["id"]
    assert response.body["data"]["user"]["email"] == decrypt.payload["email"]


def test_should_return_status_400_if_http_request_is_invalid():
    data_sut = make_sut()
    sut = data_sut.sut

    http_response = sut.handler(None)

    assert http_response.status_code == 400
    assert "error" in http_response.body["errors"]["body"].keys()
