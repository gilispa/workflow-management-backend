from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.repositories.task_repository import create_task
from app.models.project_member import ProjectMember, ProjectRole
from app.models.task import Task
from app.models.user import User
from app.repositories.task_repository import get_task_by_id, update_task_status


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

def update_task_status_for_project(
    db: Session,
    *,
    task_id: int,
    project_id: int,
    new_status,
    current_user_id: int,
) -> Task:
    task = get_task_by_id(db, task_id)

    if not task or task.project_id != project_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )

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

    return update_task_status(
        db=db,
        task=task,
        new_status=new_status,
    )