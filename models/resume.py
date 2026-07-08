from pydantic import BaseModel, EmailStr


class Profile(BaseModel):
    name: str
    email: EmailStr
    phone: str
    education: str
    current_role: str
    years_of_experience: float


class Resume(BaseModel):
    profile: Profile

    professional_summary: str

    technical_skills: list[str]

    professional_experience: list[str]

    projects: list[str]

    certifications: list[str]