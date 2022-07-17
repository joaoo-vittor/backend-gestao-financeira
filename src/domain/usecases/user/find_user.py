from abc import ABC, abstractmethod
from typing import TypedDict, Union
from src.domain.models.user import User


class LoginUserModel(TypedDict):
    """Login User Model"""

    email: str
    password: str


class LoginUserUseCase(ABC):
    @abstractmethod
    def find_user(self, user: LoginUserModel) -> Union[User, None]:
        ...
