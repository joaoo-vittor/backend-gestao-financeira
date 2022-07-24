from abc import ABC, abstractmethod
from typing import Union
from src.domain.models.user import GetUserParams, UserData


class GetUserUseCaseInterface(ABC):
    @abstractmethod
    def get_user(self, user: GetUserParams) -> Union[UserData, None]:
        raise Exception("Implementing method: get_user")
