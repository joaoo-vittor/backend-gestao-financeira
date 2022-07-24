from typing import TypedDict


class GetUserParams(TypedDict):
    """Get User Params"""

    id: int
    email: str
