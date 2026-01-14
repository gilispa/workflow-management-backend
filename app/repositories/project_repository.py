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


def get_projects_for_user(db: Session, user_id: int):
    return (
        db.query(Project)
        .join(ProjectMember)
        .filter(ProjectMember.user_id == user_id)
        .all()
    )


def get_project_by_id(
    db: Session,
    project_id: int,
) -> Project | None:
    return (
        db.query(Project)
        .filter(Project.id == project_id)
        .first()
    )