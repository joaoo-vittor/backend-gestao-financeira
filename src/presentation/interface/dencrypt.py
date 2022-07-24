from abc import ABC, abstractmethod


class Decrypt(ABC):
    @abstractmethod
    def dencrypt(self, token: str) -> dict:
        raise Exception("Implement method: dencrypt")
