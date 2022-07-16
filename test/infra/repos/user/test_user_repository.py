from src.infra.repos.user import CreateUserRepository
from src.infra.config import DBConnectionHandler
from src.infra.entities import User
from src.domain.usecases import CreateUserModel
from faker import Faker

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
    assert response["password_hash"] == fake_user["password"]
