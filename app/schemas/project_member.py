from pydantic import BaseModel, EmailStr
from app.models.project_member import ProjectRole


class AddProjectMember(BaseModel):
    email: EmailStr

class ProjectMemberResponse(BaseModel):
    user_id: int
    email: EmailStr
    role: ProjectRole

    class Config:
        from_attributes = True