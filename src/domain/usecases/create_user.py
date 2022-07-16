from abc import ABC, abstractmethod
from typing import TypedDict
from typing_extensions import NotRequired
from src.domain.models import UserModel


class CreateUserModel(TypedDict):
    """Create User Model"""

    name: NotRequired[str]
    email: str
    password: str


class CreateUser(ABC):
    @abstractmethod
    def add(self, user: CreateUserModel) -> UserModel:
        raise Exception("Implementing method: add")
