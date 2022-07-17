from sqlalchemy import Boolean, Column, String, Integer, DateTime
from sqlalchemy.sql import func
from src.infra.config import Base


class PlanModel(Base):
    """Plan Entity"""

    __tablename__ = "plan"
    __table_args__ = {"schema": "users"}

    id = Column(Integer, primary_key=True)
    type = Column(String(50), nullable=False)
    active = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self) -> str:
        return f"Plan(type={self.type}, active={self.active})"
