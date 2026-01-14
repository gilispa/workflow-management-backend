from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.api.deps import get_current_user
from app.schemas.task import TaskCreate, TaskResponse
from app.services.task_service import create_task_for_project
from app.models.user import User

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
