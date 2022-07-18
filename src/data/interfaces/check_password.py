from abc import ABC, abstractmethod


class CheckPassword(ABC):
    @abstractmethod
    def check(self, password_hash: str, password: str) -> bool:
        raise Exception("Implementing method: check")
