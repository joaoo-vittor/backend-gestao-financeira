from sqlalchemy import Column, Float, ForeignKey, Integer, DateTime, Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from src.infra.config import Base


class PlansContractModel(Base):
    """Plans Contract Entity"""

    __tablename__ = "plans_contract"
    __table_args__ = {"schema": "users"}

    id = Column(Integer, primary_key=True)
    user_id = Column(
        Integer,
        ForeignKey(
            "users.users.id",
            name="users",
        ),
        nullable=False,
    )
    plan_id = Column(
        Integer,
        ForeignKey(
            "users.plan.id",
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
    plan = relationship("PlanModel")

    def __repr__(self) -> str:
        return f"PlansContract(\
            user_id={self.user_id}\
            value_plan={self.value_plan},\
            start_time_stamp={self.start_time_stamp},\
            end_time_stamp={self.end_time_stamp},\
            active={self.active}\
            plan={self.plan})"
