from dataclasses import dataclass
from faker import Faker
from src.domain.models.user import GetUserParams
from test.infra.repos.test import GetUserRepositorySpy
from src.data.usecases.get_user import GetUserUseCase

faker = Faker()


@dataclass
class SutTypes:
    sut: GetUserUseCase
    repository: GetUserRepositorySpy


def make_sut() -> SutTypes:
    repo = GetUserRepositorySpy(None)
    sut = GetUserUseCase(repo)
    return SutTypes(sut=sut, repository=repo)


def test_should_call_get_user_with_correct_values():
    data_sut = make_sut()
    sut = data_sut.sut
    repository = data_sut.repository

    user = GetUserParams(id=faker.random_number(), email=faker.email())

    sut.get_user(user)

    assert repository.user_data["id"] == user["id"]
    assert repository.user_data["email"] == user["email"]
