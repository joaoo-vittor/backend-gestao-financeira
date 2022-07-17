from typing import TypedDict
from typing_extensions import NotRequired


class User(TypedDict):
    """User Model"""

    name: NotRequired[str]
    email: str
    password_hash: NotRequired[str]
