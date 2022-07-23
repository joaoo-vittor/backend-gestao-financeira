from abc import ABC, abstractmethod
from typing import Union
from src.domain.usecases.user import CreateUserModel
from src.domain.models.user import User


class CreateUserRespositoryInterface(ABC):
    @abstractmethod
    def create_user(self, user_data: CreateUserModel) -> Union[User, None]:
        raise Exception("Implementing method: create_user")
