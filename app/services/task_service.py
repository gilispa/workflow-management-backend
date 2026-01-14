from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.repositories.task_repository import create_task
from app.models.project_member import ProjectMember, ProjectRole
from app.models.task import Task
from app.models.user import User


def create_task_for_project(
    db: Session,
    *,
    title: str,
    description: str | None,
    project_id: int,
    assigned_to_id: int | None,
    current_user_id: int,
) -> Task:
    membership = (
        db.query(ProjectMember)
        .filter(
            ProjectMember.project_id == project_id,
            ProjectMember.user_id == current_user_id,
        )
        .first()
    )

    if not membership:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not a member of this project",
        )

    if assigned_to_id and membership.role != ProjectRole.OWNER:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only project owners can assign tasks",
        )

    if assigned_to_id:
        assignee = (
            db.query(User)
            .filter(User.id == assigned_to_id)
            .first()
        )

        if not assignee:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Assigned user not found",
            )

    return create_task(
        db=db,
        title=title,
        description=description,
        project_id=project_id,
        created_by_id=current_user_id,
        assigned_to_id=assigned_to_id,
    )
