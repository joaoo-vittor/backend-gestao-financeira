from sqlalchemy import Column, ForeignKey, String, Integer, DateTime
from sqlalchemy.sql import func
from src.infra.config import Base


class Category(Base):
    """Category Entity"""

    __tablename__ = "category"

    id = Column(Integer, primary_key=True)
    user_id = Column(
        Integer,
        ForeignKey(
            "users.id",
            name="users",
        ),
        nullable=False,
    )
    name = Column(String(128), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self) -> str:
        return f"Category(name={self.name}"
