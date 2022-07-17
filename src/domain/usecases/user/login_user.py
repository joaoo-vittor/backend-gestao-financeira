from abc import ABC, abstractmethod
from typing import TypedDict, Union
from src.domain.models.auth import Auth


class LoginUserModel(TypedDict):
    """Login User Model"""

    email: str
    password: str


class LoginUserUseCaseInterface(ABC):
    @abstractmethod
    def get_user_info(self, user: LoginUserModel) -> Union[Auth, None]:
        raise Exception("Implementing method: get_user_info")
