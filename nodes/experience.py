from state import ResumeState

from prompts.experience_prompt import EXPERIENCE_PROMPT

from utils.llm_helper import invoke_json


def enhance_experience(state: ResumeState) -> ResumeState:
    """
    Refine the candidate's professional experience while
    preserving factual accuracy.
    """

    experience = invoke_json(
        EXPERIENCE_PROMPT,
        {
            "experience": state["candidate"].experience,
            "jd_analysis": state["jd_analysis"].model_dump_json(indent=2),
        },
    )

    state["professional_experience"] = experience

    return state
