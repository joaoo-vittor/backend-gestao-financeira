from abc import ABC, abstractmethod


class Encrypter(ABC):
    @abstractmethod
    def encrypt(self, value: str) -> str:
        raise Exception("Implementing method: encrypt")
