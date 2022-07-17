from typing import TypedDict
from typing_extensions import NotRequired


class FindUserModel(TypedDict):
    """Create User Model"""

    name: NotRequired[str]
    email: str
    password: str
