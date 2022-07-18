from dataclasses import dataclass
from src.data.usecases.login_user import LoginUserUseCase
from src.domain.usecases.user import LoginUserModel
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


def test_should_call_auth_with_correct_values():
    sut_data = make_sut()
    sut = sut_data.sut
    repository = sut_data.repository
    user = LoginUserModel(email="any_email@email.com", password="any_password")

    sut.auth(user)

    assert repository.user_data["email"] == user["email"]
    assert repository.user_data["password"] == user["password"]


def test_should_return_none_if_check_password_is_invalid():
    sut_data = make_sut()
    sut = sut_data.sut
    check_password = sut_data.check_password
    user = LoginUserModel(email="any_email@email.com", password="any_password")

    check_password.is_valid = False
    response = sut.auth(user)

    assert response is None


def test_should_return_tokens_if_call_with_correct_values():
    sut_data = make_sut()
    sut = sut_data.sut

    user = LoginUserModel(email="any_email@email.com", password="any_password")
    response = sut.auth(user)

    assert "authentication" in response.keys()
    assert "authorization" in response.keys()
