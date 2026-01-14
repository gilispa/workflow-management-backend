from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.api.deps import get_current_user
from app.models.user import User
from app.schemas.project import ProjectCreate, ProjectResponse
from app.services.project_service import create_project, list_projects_for_user
from app.schemas.project_member import AddProjectMember
from app.services.project_member_service import add_project_member
from app.services.project_member_service import list_project_members
from app.schemas.project_member import ProjectMemberResponse


router = APIRouter(prefix="/projects", tags=["Projects"])


@router.post("", response_model=ProjectResponse)
def create_project_endpoint(
    project_in: ProjectCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return create_project(
        db,
        name=project_in.name,
        description=project_in.description,
        owner_id=current_user.id,
    )


@router.get("", response_model=list[ProjectResponse])
def list_my_projects(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return list_projects_for_user(db, current_user.id)


@router.post("/{project_id}/members")
def add_member(
    project_id: int,
    payload: AddProjectMember,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return add_project_member(
        db,
        project_id=project_id,
        owner_id=current_user.id,
        user_email=payload.email,
    )

@router.get(
    "/{project_id}/members",
    response_model=list[ProjectMemberResponse],
)
def get_project_members_endpoint(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return list_project_members(db, project_id)
