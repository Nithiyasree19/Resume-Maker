from state import ResumeState

from prompts.summary_prompt import SUMMARY_PROMPT

from utils.llm_helper import invoke_text


def generate_professional_summary(state: ResumeState) -> ResumeState:
    """
    Generate a role-specific professional summary.
    """

    summary = invoke_text(
        SUMMARY_PROMPT,
        {
            "candidate_analysis": state["candidate_analysis"].model_dump_json(indent=2),
            "jd_analysis": state["jd_analysis"].model_dump_json(indent=2),
        },
    )

    state["professional_summary"] = summary

    return state