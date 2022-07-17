from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.sql import func
from src.infra.config import Base


class PaymentMethod(Base):
    """PaymentMethod Entity"""

    __tablename__ = "payment_method"
    __table_args__ = {"schema": "expenses"}

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self) -> str:
        return f"PaymentMethod(name={self.name}"
