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
