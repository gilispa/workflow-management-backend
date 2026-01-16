from sqlalchemy.orm import Session
from app.models.task import Task


def create_task(
    db: Session,
    *,
    title: str,
    description: str | None,
    project_id: int,
    created_by_id: int,
    assigned_to_id: int | None,
) -> Task:
    task = Task(
        title=title,
        description=description,
        project_id=project_id,
        created_by_id=created_by_id,
        assigned_to_id=assigned_to_id,
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


def get_task_by_id(db: Session, task_id: int) -> Task | None:
    return db.query(Task).filter(Task.id == task_id).first()


def update_task_status(
    db: Session,
    task: Task,
    new_status,
) -> Task:
    task.status = new_status
    db.commit()
    db.refresh(task)
    return task