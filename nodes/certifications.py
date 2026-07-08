from state import ResumeState

from prompts.certifications_prompt import CERTIFICATIONS_PROMPT

from utils.llm_helper import invoke_json


def organize_certifications(state: ResumeState) -> ResumeState:
    """
    Organize certifications based on
    relevance to the target job.
    """

    certifications = invoke_json(
        CERTIFICATIONS_PROMPT,
        {
            "certifications": state["candidate"].certifications,
            "jd_analysis": state["jd_analysis"].model_dump_json(indent=2),
        },
    )

    state["certifications"] = certifications

    return state