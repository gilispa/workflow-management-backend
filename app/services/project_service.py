from sqlalchemy.orm import Session
from app.repositories.project_repository import create_project_with_owner
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
