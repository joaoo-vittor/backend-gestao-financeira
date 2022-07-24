from typing import TypedDict


class Plan(TypedDict):
    """Plan"""

    type: str
    active: bool


class PlanContract(TypedDict):
    """Plan Contract"""

    user_id: int
    plan_id: int
    value_plan: float
    start_time_stamp: str
    end_time_stamp: str
    active: bool
    plan: Plan
