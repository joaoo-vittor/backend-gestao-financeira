from abc import ABC, abstractmethod
from typing import Union
from src.domain.usecases.user import LoginUserModel
from src.domain.models.user import User


class FindUserRespositoryInterface(ABC):
    @abstractmethod
    def find_user(self, user_data: LoginUserModel) -> Union[User, None]:
        raise Exception("Implementing method: find_user")
