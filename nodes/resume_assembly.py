from state import ResumeState

from models.resume import Resume


def assemble_resume(state: ResumeState) -> ResumeState:
    """
    Assemble the final resume from all generated sections.
    """

    candidate = state["candidate"]

    resume = Resume(
        profile={
            "name": candidate.name,
            "email": candidate.email,
            "phone": candidate.phone,
            "education": candidate.education,
            "current_role": candidate.current_role,
            "years_of_experience": candidate.years_of_experience,
        },
        professional_summary=state["professional_summary"],
        technical_skills=state["technical_skills"],
        professional_experience=state["professional_experience"],
        projects=state["projects"],
        certifications=state["certifications"],
    )

    state["resume"] = resume

    return state