from typing import TypedDict


class LoginUserModel(TypedDict):
    """Login User Model"""

    email: str
    password: str
