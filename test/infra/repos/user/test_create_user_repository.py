from faker import Faker
import pytest
from src.infra.repos.user import CreateUserRepository
from src.infra.config import DBConnectionHandler
from src.domain.usecases.user import CreateUserModel

faker = Faker()

CONNECTION_STRING_TEST = (
    "postgresql+pg8000://postgres:mysecretpassword@127.0.0.1:5433/postgres"
)


def make_sut() -> CreateUserRepository:
    connection_handler = DBConnectionHandler(CONNECTION_STRING_TEST)
    return CreateUserRepository(connection_handler)


@pytest.fixture
def drop_database():
    connection_handler = DBConnectionHandler(CONNECTION_STRING_TEST)
    engine = connection_handler.get_engine()
    yield
    engine.execute("DELETE FROM users.users")


def make_create_user_model():
    return CreateUserModel(
        name=faker.name(), email=faker.email(), password=faker.password()
    )


def test_should_return_user_model_if_user_was_inserted(drop_database):
    sut = make_sut()
    fake_user = make_create_user_model()

    response = sut.create_user(fake_user)

    assert response["email"] == fake_user["email"]
    assert response["name"] == fake_user["name"]


def test_should_return_user_model_without_name_if_user_without_name_was_inserted(
    drop_database,
):
    sut = make_sut()
    fake_user = CreateUserModel(email=faker.email(), password=faker.password())

    response = sut.create_user(fake_user)

    assert response["email"] == fake_user["email"]
    assert response["name"] is None


def test_should_return_none_if_pass_none():
    sut = make_sut()
    fake_user = None

    response = sut.create_user(fake_user)

    assert response is None


def test_should_raise_exeception_if_insert_two_some_emails(drop_database):
    sut = make_sut()
    fake_user = make_create_user_model()

    with pytest.raises(Exception) as info_err:
        sut.create_user(fake_user)
        sut.create_user(fake_user)

    assert info_err.typename == "IntegrityError"
