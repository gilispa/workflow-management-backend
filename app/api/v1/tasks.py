from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.api.deps import get_current_user
from app.schemas.task import TaskCreate, TaskResponse
from app.services.task_service import create_task_for_project
from app.models.user import User
from app.schemas.task import TaskUpdateStatus
from app.services.task_service import update_task_status_for_project
from app.services.task_service import get_tasks_for_project

router = APIRouter(prefix="/projects/{project_id}/tasks", tags=["Tasks"])


@router.post("", response_model=TaskResponse)
def create_task_endpoint(
    project_id: int,
    task_in: TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return create_task_for_project(
        db=db,
        title=task_in.title,
        description=task_in.description,
        project_id=project_id,
        assigned_to_id=task_in.assigned_to_id,
        current_user_id=current_user.id,
    )


@router.patch(
    "/{task_id}/status",
    response_model=TaskResponse,
)
def update_task_status_endpoint(
    project_id: int,
    task_id: int,
    task_in: TaskUpdateStatus,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return update_task_status_for_project(
        db=db,
        task_id=task_id,
        project_id=project_id,
        new_status=task_in.status,
        current_user_id=current_user.id,
    )

@router.get("", response_model=list[TaskResponse])
def get_tasks_endpoint(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_tasks_for_project(
        db=db,
        project_id=project_id,
        current_user_id=current_user.id,
    )