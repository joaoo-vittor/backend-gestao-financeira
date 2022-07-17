from abc import ABC, abstractmethod
from typing import Union
from src.domain.usecases.user import LoginUserModel
from src.domain.models.user import UserLogin


class LoginUserRespositoryInterface(ABC):
    @abstractmethod
    def find_user(self, user_data: LoginUserModel) -> Union[UserLogin, None]:
        raise Exception("Implementing method: find_user")
