from abc import ABC, abstractmethod
from typing import TypedDict, Union
from typing_extensions import NotRequired
from src.domain.models.user import UserModel


class CreateUserModel(TypedDict):
    """Create User Model"""

    name: NotRequired[str]
    email: str
    password: str


class CreateUserInterface(ABC):
    @abstractmethod
    def add(self, user: CreateUserModel) -> Union[UserModel, None]:
        raise Exception("Implementing method: add")
