from sqlalchemy.orm import Session
from app.models.project import Project
from app.models.project_member import ProjectMember, ProjectRole


def create_project_with_owner(
    db: Session,
    name: str,
    description: str | None,
    owner_id: int,
) -> Project:
    project = Project(
        name=name,
        description=description,
        owner_id=owner_id,
    )
    db.add(project)
    db.flush()

    member = ProjectMember(
        user_id=owner_id,
        project_id=project.id,
        role=ProjectRole.OWNER,
    )
    db.add(member)

    db.commit()
    db.refresh(project)

    return project
