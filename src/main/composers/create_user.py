from src.infra.config import DBConnectionHandler
from src.infra.repos.user import CreateUserRepository
from src.data.usecases.create_user import CreateUserUseCase
from src.infra.helpers.criptography import Encrypter
from src.presentation.controllers.create_user import CreateUserController
from src.presentation.helpers.validators import ValidatorBodyCreateUser
from src.settings import CONNECTION_STRING


def create_user_compose() -> CreateUserController:
    db_handler = DBConnectionHandler(CONNECTION_STRING)
    repository = CreateUserRepository(db_handler)
    encrypter = Encrypter()
    usecase = CreateUserUseCase(repository, encrypter)
    validator = ValidatorBodyCreateUser()
    controller = CreateUserController(usecase, validator)
    return controller
