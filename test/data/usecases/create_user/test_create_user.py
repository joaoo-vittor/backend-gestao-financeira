from dataclasses import dataclass
from faker import Faker
from src.data.usecases.create_user import CreateUserUseCase
from test.infra.repos.test import CreateUserRepositorySpy
from src.data.interfaces import Encrypter
from src.domain.usecases import CreateUserModel

faker = Faker()


@dataclass
class SutType:
    sut: CreateUserUseCase
    repository: CreateUserRepositorySpy
    encrypt: Encrypter


class EncrypterSpy(Encrypter):
    def __init__(self) -> None:
        self.value: str = ""

    def encrypt(self, value: str) -> str:
        self.value = value
        return "hashed_password"


def make_sut() -> SutType:
    encrypt = EncrypterSpy()
    repo = CreateUserRepositorySpy(None)
    sut = CreateUserUseCase(repo, encrypt)
    return SutType(sut=sut, repository=repo, encrypt=encrypt)


def test_should_call_add_with_correct_values():
    sut_data = make_sut()
    sut = sut_data.sut
    repository = sut_data.repository

    user = CreateUserModel(
        name=faker.name(), email=faker.email(), password=faker.password()
    )

    response = sut.add(user)

    assert response["email"] == repository.user_data["email"]
    assert response["name"] == repository.user_data["name"]
    assert repository.user_data["password"] == "hashed_password"
