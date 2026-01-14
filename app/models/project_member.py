import enum

from sqlalchemy import Column, Integer, DateTime, ForeignKey, Enum
from sqlalchemy.sql import func

from app.db.base import Base


class ProjectRole(str, enum.Enum):
    OWNER = "OWNER"
    MEMBER = "MEMBER"


class ProjectMember(Base):
    __tablename__ = "project_members"

    id = Column(Integer, primary_key=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )

    project_id = Column(
        Integer,
        ForeignKey("projects.id", ondelete="CASCADE"),
        nullable=False
    )

    role = Column(
        Enum(ProjectRole),
        nullable=False
    )

    joined_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )
