from abc import ABC, abstractmethod
from typing import TypedDict, Union
from typing_extensions import NotRequired
from src.domain.models.user import User


class CreateUserModel(TypedDict):
    """Create User Model"""

    name: NotRequired[str]
    email: str
    password: str


class CreateUserUseCaseInterface(ABC):
    @abstractmethod
    def add(self, user: CreateUserModel) -> Union[User, None]:
        raise Exception("Implementing method: add")
