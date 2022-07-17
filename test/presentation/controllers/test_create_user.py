from dataclasses import dataclass
from typing import Any
from faker import Faker
from src.presentation.helpers.http import HttpRequest
from src.presentation.interface import Validator
from src.presentation.controllers.create_user import CreateUserController
from test.infra.repos.test import CreateUserRepositorySpy
from test.data.usecases.test import CreateUserUseCaseSpy
from src.data.interfaces import Encrypter

faker = Faker()


class EncrypterSpy(Encrypter):
    def encrypt(self, value: str) -> str:
        return "hashed_password"


class ValidatorBadyCreateUserSpy(Validator):
    def __init__(self) -> None:
        self.valid = True

    def validate(self, data: dict) -> bool:
        return self.valid


@dataclass
class SutTypes:
    sut: CreateUserController
    validator: ValidatorBadyCreateUserSpy


def make_sut() -> SutTypes:
    repo = CreateUserRepositorySpy(None)
    encrypter = EncrypterSpy()
    validator = ValidatorBadyCreateUserSpy()
    usecase = CreateUserUseCaseSpy(repo, encrypter)
    controller = CreateUserController(usecase, validator)
    return SutTypes(sut=controller, validator=validator)


class CreateUserUseCaseSpyWithException:
    def __init__(self, repo, encrypter) -> None:
        ...

    def add(self, user: Any) -> Any:
        raise Exception("")


def make_sut_with_exception() -> SutTypes:
    repo = CreateUserRepositorySpy(None)
    encrypter = EncrypterSpy()
    validator = ValidatorBadyCreateUserSpy()
    usecase = CreateUserUseCaseSpyWithException(repo, encrypter)
    controller = CreateUserController(usecase, validator)
    return SutTypes(sut=controller, validator=validator)


def make_http_request():
    return HttpRequest(
        body={
            "name": faker.name(),
            "email": faker.email(),
            "password": faker.password(),
        }
    )


def test_should_return_status_200_and_data_if_http_request_is_valid():
    sut = make_sut().sut
    http_request = make_http_request()
    response = sut.handler(http_request)

    assert response.status_code == 200
    assert response.body["data"]["user"]["name"] == http_request.body["name"]
    assert response.body["data"]["user"]["email"] == http_request.body["email"]


def test_should_return_status_400_if_body_is_none():
    sut = make_sut().sut
    response = sut.handler(None)
    assert response.status_code == 400
    assert response.body["errors"]["status_code"] == 400


def test_should_return_status_422_if_body_is_invalid():
    sut_data = make_sut()
    sut = sut_data.sut
    validator = sut_data.validator
    http_request = make_http_request()

    validator.valid = False
    response = sut.handler(http_request)

    assert response.status_code == 422
    assert response.body["errors"]["status_code"] == 422


def test_should_return_status_500_if_raise_exception():
    sut = make_sut_with_exception().sut
    http_request = make_http_request()
    response = sut.handler(http_request)

    assert response.status_code == 500
    assert response.body["errors"]["status_code"] == 500
