from sqlalchemy.orm import Session
from app.models.task import Task
from sqlalchemy import func


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


def get_task_by_id(db: Session, task_id: int):
    return (
        db.query(Task)
        .filter(
            Task.id == task_id,
            Task.is_deleted == False,
        )
        .first()
    )



def update_task_status(
    db: Session,
    task: Task,
    new_status,
) -> Task:
    task.status = new_status
    db.commit()
    db.refresh(task)
    return task

def get_tasks_by_project(db: Session, project_id: int) -> list[Task]:
    return db.query(Task).filter(Task.project_id == project_id).all()


def get_tasks_filtered(
    db: Session,
    *,
    project_id: int,
    status=None,
    assignee_id=None,
):
    query = db.query(Task).filter(Task.project_id == project_id)

    if status is not None:
        query = query.filter(Task.status == status)

    if assignee_id is not None:
        query = query.filter(Task.assigned_to_id == assignee_id)

    return query.all()


def soft_delete_task(
    db: Session,
    task: Task,
) -> Task:
    task.is_deleted = True
    task.deleted_at = func.now()
    db.commit()
    db.refresh(task)
    return task
