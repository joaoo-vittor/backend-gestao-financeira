from abc import ABC, abstractmethod
from typing import Union
from src.domain.usecases.user import FindUserModel
from src.domain.models.user import UserModel


class FindUserRespositoryInterface(ABC):
    @abstractmethod
    def find_user(self, user_data: FindUserModel) -> Union[UserModel, None]:
        raise Exception("Implementing method: find_user")
