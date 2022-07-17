from typing import TypedDict


class PlanContract(TypedDict):
    """Plan Contract"""

    user_id: int
    plan_id: int
    value_plan: float
    start_time_stamp: str
    end_time_stamp: str
    active: bool
