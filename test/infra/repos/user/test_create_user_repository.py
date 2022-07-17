from faker import Faker
import pytest
from src.infra.repos.user import CreateUserRepository
from src.infra.config import DBConnectionHandler
from src.infra.entities import User
from src.domain.usecases import CreateUserModel

faker = Faker()


def make_sut() -> CreateUserRepository:
    connection_handler = DBConnectionHandler("sqlite:///:memory:")
    engine = connection_handler.get_engine()
    User.metadata.create_all(bind=engine)
    return CreateUserRepository(connection_handler)


def make_create_user_model():
    return CreateUserModel(
        name=faker.name(), email=faker.email(), password=faker.password()
    )


def test_should_return_user_model_if_user_was_inserted():
    sut = make_sut()
    fake_user = make_create_user_model()

    response = sut.create_user(fake_user)

    assert response["email"] == fake_user["email"]
    assert response["name"] == fake_user["name"]


def test_should_return_user_model_without_name_if_user_without_name_was_inserted():
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


def test_should_raise_exeception_if_insert_two_some_emails():
    sut = make_sut()
    fake_user = make_create_user_model()

    sut.create_user(fake_user)
    with pytest.raises(Exception) as info_err:
        sut.create_user(fake_user)

    assert info_err.typename == "IntegrityError"
