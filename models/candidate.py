from pydantic import BaseModel, EmailStr
from typing import List


class Candidate(BaseModel):
    name: str
    email: EmailStr
    phone: str
    education: str
    current_role: str
    years_of_experience: float

    skills: List[str]
    experience: List[str]
    projects: List[str]
    certifications: List[str]