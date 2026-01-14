from sqlalchemy.orm import Session
from app.models.project_member import ProjectMember
from app.models.project_member import ProjectRole
from app.models.user import User


def add_member_to_project(
    db: Session,
    *,
    user_id: int,
    project_id: int,
    role: ProjectRole = ProjectRole.MEMBER,
) -> ProjectMember:
    member = ProjectMember(
        user_id=user_id,
        project_id=project_id,
        role=role,
    )
    db.add(member)
    db.commit()
    db.refresh(member)
    return member


def is_user_already_member(
    db: Session,
    *,
    user_id: int,
    project_id: int,
) -> bool:
    return (
        db.query(ProjectMember)
        .filter(
            ProjectMember.user_id == user_id,
            ProjectMember.project_id == project_id,
        )
        .first()
        is not None
    )

def is_project_owner(
    db: Session,
    *,
    project_id: int,
    user_id: int,
) -> bool:
    return (
        db.query(ProjectMember)
        .filter(
            ProjectMember.project_id == project_id,
            ProjectMember.user_id == user_id,
            ProjectMember.role == ProjectRole.OWNER,
        )
        .first()
        is not None
    )


def get_project_members(
    db: Session,
    project_id: int,
):
    return (
        db.query(ProjectMember, User)
        .join(User, ProjectMember.user_id == User.id)
        .filter(ProjectMember.project_id == project_id)
        .all()
    )