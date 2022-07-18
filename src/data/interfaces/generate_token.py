from abc import ABC, abstractmethod


class GenerateToken(ABC):
    @abstractmethod
    def generate_token(self, payload: dict) -> str:
        raise Exception("Implementing method: check")
