from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.project_member import ProjectMember
from app.repositories.project_member_repository import (
    add_member_to_project,
    is_user_already_member,
    get_project_members
)
from app.repositories.project_repository import (
    get_project_by_id,
)
from app.repositories.user_repository import get_user_by_email
from app.repositories.project_member_repository import is_project_owner


def add_project_member(
    db: Session,
    *,
    project_id: int,
    owner_id: int,
    user_email: str,
) -> ProjectMember:

    project = get_project_by_id(db, project_id)

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    if not is_project_owner(db, project_id=project_id, user_id=owner_id):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only project owner can add members",
        )

    user = get_user_by_email(db, email=user_email)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if is_user_already_member(
        db,
        user_id=user.id,
        project_id=project_id,
    ):
        raise HTTPException(
            status_code=400,
            detail="User already member of project",
        )

    return add_member_to_project(
        db,
        user_id=user.id,
        project_id=project_id,
        role="MEMBER",
    )


def list_project_members(
    db: Session,
    project_id: int,
):
    members = get_project_members(db, project_id)

    return [
        {
            "user_id": user.id,
            "email": user.email,
            "role": member.role,
        }
        for member, user in members
    ]