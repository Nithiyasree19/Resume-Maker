from state import ResumeState

from prompts.projects_prompt import PROJECTS_PROMPT

from utils.llm_helper import invoke_json


def generate_projects(state: ResumeState) -> ResumeState:
    """
    Select and rewrite the candidate's projects
    based on relevance to the target job description.
    """

    projects = invoke_json(
        PROJECTS_PROMPT,
        {
            "projects": state["candidate"].projects,
            "jd_analysis": state["jd_analysis"].model_dump_json(indent=2),
        },
    )

    state["projects"] = projects

    return state