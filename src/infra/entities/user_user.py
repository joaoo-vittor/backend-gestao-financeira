from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.sql import func
from src.infra.config import Base


class User(Base):
    """User Entity"""

    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=True)
    email = Column(String(255), nullable=False, unique=True)
    password_hash = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self) -> str:
        return f"User(name={self.user_name}, email={self.email})"