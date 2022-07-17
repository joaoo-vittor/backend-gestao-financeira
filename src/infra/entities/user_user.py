from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from src.infra.config import Base


class UserModel(Base):
    """User Entity"""

    __tablename__ = "users"
    __table_args__ = {"schema": "users"}

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=True)
    email = Column(String(255), nullable=False, unique=True)
    password_hash = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    plan_contract = relationship("PlansContractModel")

    def __repr__(self) -> str:
        return f"Users(id={self.id},\
            name={self.name},\
            email={self.email},\
            plan_contract={self.plan_contract})"
