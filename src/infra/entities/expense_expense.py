from sqlalchemy import Column, Float, ForeignKey, String, Integer, DateTime
from sqlalchemy.sql import func
from src.infra.config import Base


class Expense(Base):
    """Expense Entity"""

    __tablename__ = "expense"

    id = Column(Integer, primary_key=True)
    user_id = Column(
        Integer,
        ForeignKey(
            "user.user.id",
            name="user",
        ),
        nullable=False,
    )
    category_id = Column(
        Integer,
        ForeignKey(
            "expense.category.id",
            name="category",
        ),
        nullable=False,
    )
    payment_method_id = Column(
        Integer,
        ForeignKey(
            "expense.payment_method.id",
            name="payment_method",
        ),
        nullable=False,
    )
    name = Column(String(128), nullable=False)
    value = Column(Float, nullable=False)
    status = Column(String(128), nullable=False)
    time_stamp = Column(DateTime(timezone=True), nullable=False)
    voucher = Column(String(255), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self) -> str:
        return f"Expense(name={self.name},\
            value={self.value},\
            status={self.value},\
            time_stamp={self.time_stamp},\
            voucher={self.voucher})"
