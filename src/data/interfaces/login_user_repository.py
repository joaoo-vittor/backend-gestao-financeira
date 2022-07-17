from abc import ABC, abstractmethod
from typing import Union
from src.domain.usecases.user import CreateUserModel
from src.domain.models.user import UserModel


class FindUserRespositoryInterface(ABC):
    @abstractmethod
    def find_user(self, user_data: CreateUserModel) -> Union[UserModel, None]:
        raise Exception("Implementing method: find_user")
