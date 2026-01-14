from sqlalchemy.orm import Session
from app.repositories.project_repository import (
    create_project_with_owner,
    get_projects_for_user,
)
from app.models.project import Project


def create_project(
    db: Session,
    name: str,
    description: str | None,
    owner_id: int,
) -> Project:
    return create_project_with_owner(
        db=db,
        name=name,
        description=description,
        owner_id=owner_id,
    )


def list_projects_for_user(
    db: Session,
    user_id: int,
) -> list[Project]:
    return get_projects_for_user(db, user_id)
