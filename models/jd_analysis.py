from pydantic import BaseModel
from typing import List


class JDAnalysis(BaseModel):
    required_skills: List[str]
    preferred_technologies: List[str]
    domain_keywords: List[str]
    role_expectations: List[str]
    ats_keywords: List[str]