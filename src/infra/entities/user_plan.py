from sqlalchemy import Boolean, Column, String, Integer, DateTime
from sqlalchemy.sql import func
from src.infra.config import Base


class Plan(Base):
    """Plan Entity"""

    __tablename__ = "plan"

    id = Column(Integer, primary_key=True)
    _type = Column(String(50), nullable=False)
    active = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self) -> str:
        return f"Plan(type={self._type}, active={self.active})"
