from src.infra.config.db_config import DBConnectionHandler
from src.settings.envs import CONNECTION_STRING
from src.infra.repos.user import GetUserRepository
from src.data.usecases.get_user import GetUserUseCase
from src.infra.helpers.dencrypt import DecryptToken
from src.presentation.helpers.validators import ValidatorHeaderGetUser
from src.presentation.controllers.get_user import GetUserController


def get_user_compose() -> GetUserController:
    db_handler = DBConnectionHandler(CONNECTION_STRING)
    repository = GetUserRepository(db_handler)
    use_case = GetUserUseCase(repository)
    decrypt = DecryptToken()
    validator = ValidatorHeaderGetUser()
    return GetUserController(use_case, validator, decrypt)
