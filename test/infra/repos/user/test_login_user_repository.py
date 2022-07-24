from faker import Faker
import pytest
from src.infra.repos.user import LoginUserRepository
from src.infra.config import DBConnectionHandler
from src.domain.usecases.user import LoginUserModel

faker = Faker()

CONNECTION_STRING_TEST = (
    "postgresql+pg8000://postgres:mysecretpassword@127.0.0.1:5433/postgres"
)


def make_sut() -> LoginUserRepository:
    connection_handler = DBConnectionHandler(CONNECTION_STRING_TEST)
    return LoginUserRepository(connection_handler)


@pytest.fixture
def drop_database():
    connection_handler = DBConnectionHandler(CONNECTION_STRING_TEST)
    engine = connection_handler.get_engine()
    engine.execute("DELETE FROM users.users")
    engine.execute(
        "INSERT INTO users.users(id, email, password_hash)\
        VALUES ('1', 'any_email@email.com', 'any_password')"
    )
    engine.execute(
        "INSERT INTO users.plans_contract(id, user_id, plan_id, value_plan, start_time_stamp, end_time_stamp)\
        VALUES ('1', '1', '1', '0.0',current_date, current_date + INTERVAL '2 day')"
    )
    engine.execute(
        "INSERT INTO users.plans_contract(id, user_id, plan_id, value_plan, start_time_stamp, end_time_stamp)\
        VALUES ('2', '1', '1', '1.0',current_date, current_date + INTERVAL '4 day')"
    )
    yield
    engine.execute("DELETE FROM users.users")


def test_should_return_none_if_pass_none_to_find_user():
    sut = make_sut()
    response = sut.find_user(None)

    assert response is None


def test_should_return_user_model_if_call_find_user_with_valid_values(drop_database):
    sut = make_sut()
    email = "any_email@email.com"
    user = LoginUserModel(email=email, password="any_password")
    response = sut.find_user(user)

    assert response["email"] == email
    assert response["plan_contract"]["plan"]["type"] == "Freemium"
    assert response["plan_contract"]["plan"]["active"] is True


def test_should_return_none_if_find_user_not_find(drop_database):
    sut = make_sut()
    email = "any_email1@email.com"
    user = LoginUserModel(email=email, password="any_password")
    response = sut.find_user(user)

    assert response is None
