from dataclasses import dataclass
from faker import Faker
from src.presentation.helpers import HttpRequest
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
    encripter = EncrypterSpy()
    validator = ValidatorBadyCreateUserSpy()
    usecase = CreateUserUseCaseSpy(repo, encripter)
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


def test_should_return_status_422_if_body_is_invalid():
    sut_data = make_sut()
    sut = sut_data.sut
    validator = sut_data.validator
    http_request = make_http_request()

    validator.valid = False
    response = sut.handler(http_request)

    assert response.status_code == 422
