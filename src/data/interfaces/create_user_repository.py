from abc import ABC, abstractmethod
from typing import Union
from src.domain.usecases import CreateUserModel
from src.domain.models import UserModel


class CreateUserRespositoryInterface(ABC):
    @abstractmethod
    def create_user(self, user_data: CreateUserModel) -> Union[UserModel, None]:
        raise Exception("Implementing method: create_user")
