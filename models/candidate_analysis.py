from pydantic import BaseModel
from typing import List


class CandidateAnalysis(BaseModel):
    matching_skills: List[str]
    relevant_experience: List[str]
    relevant_projects: List[str]
    relevant_certifications: List[str]