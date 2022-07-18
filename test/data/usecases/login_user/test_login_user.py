from dataclasses import dataclass
from src.data.usecases.login_user import LoginUserUseCase
from test.infra.repos.test import LoginUserRepositorySpy
from src.data.interfaces import CheckPassword, GenerateToken


class CheckPasswordSpy(CheckPassword):
    def __init__(self) -> None:
        self.password_hash = None
        self.password = None
        self.is_valid = True

    def check(self, password_hash: str, password: str) -> bool:
        self.password_hash = password_hash
        self.password = password
        return self.is_valid


class GenerateTokenSpy(GenerateToken):
    def __init__(self) -> None:
        self.payload = None

    def generate_token(self, payload: dict) -> str:
        self.payload = payload
        return "any_token"


@dataclass
class SutTypes:
    sut: LoginUserUseCase
    check_password: CheckPasswordSpy
    generate_token: GenerateTokenSpy
    repository: LoginUserRepositorySpy


def make_sut() -> SutTypes:
    repo = LoginUserRepositorySpy(None)
    check_password = CheckPasswordSpy()
    generate_token = GenerateTokenSpy()
    usecase = LoginUserUseCase(repo, check_password, generate_token)
    return SutTypes(
        sut=usecase,
        check_password=check_password,
        generate_token=generate_token,
        repository=repo,
    )


def test_should_return_none_if_call_auth_with_none():
    sut = make_sut().sut

    response = sut.auth(None)

    assert response is None
