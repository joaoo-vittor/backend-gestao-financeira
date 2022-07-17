from typing import Type
from abc import ABC, abstractmethod
from src.presentation.helpers.http import HttpRequest, HttpResponse


class HandlerInterface(ABC):
    """Interface to Handlers"""

    @abstractmethod
    def handler(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Defining Handler"""

        raise Exception("Implement method: handler")
