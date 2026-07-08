from state import ResumeState

from prompts.skills_prompt import SKILLS_PROMPT

from utils.llm_helper import invoke_json


def optimize_skills(state: ResumeState) -> ResumeState:
    """
    Organize the candidate's technical skills based on
    relevance to the target job description.
    """

    skills = invoke_json(
        SKILLS_PROMPT,
        {
            "candidate": state["candidate"].model_dump_json(indent=2),
            "jd_analysis": state["jd_analysis"].model_dump_json(indent=2),
        },
    )

    state["technical_skills"] = skills

    return state