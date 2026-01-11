import enum

from sqlalchemy import Column, Integer, String, Boolean, DateTime, Enum
from sqlalchemy.sql import func

from app.db.base import Base


class UserRole(str, enum.Enum):
    ADMIN = "ADMIN"
    MEMBER = "MEMBER"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    email = Column(String, unique=True, nullable=False, index=True)
    password_hash = Column(String, nullable=False)

    is_active = Column(Boolean, default=True)

    role = Column(
        Enum(UserRole),
        nullable=False,
        default=UserRole.MEMBER
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )
