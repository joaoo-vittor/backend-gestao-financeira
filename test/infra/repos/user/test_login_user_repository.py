from faker import Faker
from src.infra.repos.user import LoginUserRepository
from src.infra.config import DBConnectionHandler


faker = Faker()

CONNECTION_STRING_TEST = (
    "postgresql+pg8000://postgres:mysecretpassword@127.0.0.1:5433/postgres"
)


def make_sut() -> LoginUserRepository:
    connection_handler = DBConnectionHandler(CONNECTION_STRING_TEST)
    return LoginUserRepository(connection_handler)


def test_should_return_none_if_pass_none_to_find_user():
    sut = make_sut()
    response = sut.find_user(None)

    assert response is None
