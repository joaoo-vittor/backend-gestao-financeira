from sqlalchemy import Column, Float, ForeignKey, Integer, DateTime, Boolean
from sqlalchemy.sql import func
from src.infra.config import Base


class PlansContract(Base):
    """Plans Contract Entity"""

    __tablename__ = "plans_contract"

    id = Column(Integer, primary_key=True)
    user_id = Column(
        Integer,
        ForeignKey(
            "users.id",
            name="users",
        ),
        nullable=False,
    )
    plan_id = Column(
        Integer,
        ForeignKey(
            "plan.id",
            name="users",
        ),
        nullable=False,
    )
    value_plan = Column(Float, nullable=False)
    start_time_stamp = Column(DateTime(timezone=True), server_default=func.now())
    end_time_stamp = Column(DateTime(timezone=True))
    active = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self) -> str:
        return f"PlansContract(value_plan={self.value_plan},\
            start_time_stamp={self.start_time_stamp},\
            end_time_stamp={self.end_time_stamp},\
            active={self.active})"
