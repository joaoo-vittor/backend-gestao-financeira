from faker import Faker
import pytest
from src.domain.models.user import GetUserParams
from src.infra.repos.user import GetUserRepository
from src.infra.config import DBConnectionHandler

faker = Faker()

CONNECTION_STRING_TEST = (
    "postgresql+pg8000://postgres:mysecretpassword@127.0.0.1:5433/postgres"
)


def make_sut() -> GetUserRepository:
    connection_handler = DBConnectionHandler(CONNECTION_STRING_TEST)
    return GetUserRepository(connection_handler)


@pytest.fixture
def drop_database():
    connection_handler = DBConnectionHandler(CONNECTION_STRING_TEST)
    engine = connection_handler.get_engine()
    yield engine
    engine.execute("DELETE FROM users.users")


def make_user_data(drop_database) -> dict:
    data_user = {
        "id": faker.random_number(digits=2),
        "password_hash": faker.password(),
        "email": faker.email(),
    }

    insert_user_query = "INSERT INTO\
        users.users(id, email, password_hash)\
        VALUES ('{id}','{email}','{password_hash}')".format(
        **data_user
    )
    plans_contract_query = "INSERT INTO\
        users.plans_contract(id, user_id, plan_id, value_plan,\
            start_time_stamp, end_time_stamp)\
        VALUES ('1', '{id}', '1', '0.0',\
        current_date, current_date + INTERVAL '2 day')".format(
        id=data_user["id"]
    )

    drop_database.execute(insert_user_query)
    drop_database.execute(plans_contract_query)

    return data_user


def test_should_return_user_data_if_email_and_id_is_correct(drop_database):
    user_data = make_user_data(drop_database)
    sut = make_sut()

    user_params = GetUserParams(id=user_data["id"], email=user_data["email"])
    response = sut.find_user_by(user_params)

    assert response["id"] == user_data["id"]
    assert response["email"] == user_data["email"]
