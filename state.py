from typing import TypedDict

from models.candidate import Candidate
from models.jd_analysis import JDAnalysis
from models.candidate_analysis import CandidateAnalysis
from models.resume import Resume


class ResumeState(TypedDict):
    # Initial Inputs
    candidate: Candidate
    job_description: str

    # Intermediate Outputs
    jd_analysis: JDAnalysis
    candidate_analysis: CandidateAnalysis

    professional_summary: str
    technical_skills: list[str]
    professional_experience: list[str]
    projects: list[str]
    certifications: list[str]

    # Final Output
    resume: Resume