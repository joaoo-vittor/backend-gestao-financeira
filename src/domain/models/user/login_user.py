from typing import TypedDict
from typing_extensions import NotRequired
from src.domain.models.user import PlanContract, Plan


class UserLogin(TypedDict):
    """User Model"""

    name: NotRequired[str]
    email: str
    password_hash: NotRequired[str]
    plan_contract: PlanContract
    plan: Plan
