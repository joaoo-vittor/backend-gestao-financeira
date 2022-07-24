from abc import ABC, abstractmethod
from typing import Union
from src.domain.models.user import GetUserParams, UserData


class GetUserRepositoryInterface(ABC):
    """GetUser Repository Interface"""

    @abstractmethod
    def find_user_by(self, user_params: GetUserParams) -> Union[UserData, None]:
        raise Exception("Implementing method: find_user_by")
