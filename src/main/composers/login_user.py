from src.infra.config import DBConnectionHandler
from src.infra.repos.user import LoginUserRepository
from src.data.usecases.login_user import LoginUserUseCase
from src.infra.helpers.check_password import CheckPassword
from src.infra.helpers.generate_token import GenerateToken
from src.presentation.controllers.login_user import LoginUserController
from src.presentation.helpers.validators import ValidatorBodyLoginUser
from src.settings import CONNECTION_STRING


def login_user_compose() -> LoginUserController:
    db_handler = DBConnectionHandler(CONNECTION_STRING)
    repository = LoginUserRepository(db_handler)
    check_password = CheckPassword()
    generate_token = GenerateToken()
    usecase = LoginUserUseCase(repository, check_password, generate_token)
    validator = ValidatorBodyLoginUser()
    return LoginUserController(usecase, validator)
