from abc import ABC, abstractmethod
from typing import Union
from src.domain.models.user import GetUserParams
from src.domain.models.user import UserLogin


class GetUserRepositoryInterface(ABC):
    """GetUser Repository Interface"""

    @abstractmethod
    def find_user_by(self, user_params: GetUserParams) -> Union[UserLogin, None]:
        ...
