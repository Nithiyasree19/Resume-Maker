from state import ResumeState

from models.jd_analysis import JDAnalysis

from prompts.jd_analysis_prompt import JD_ANALYSIS_PROMPT

from utils.llm_helper import invoke_json


def analyze_jd(state: ResumeState) -> ResumeState:
    """
    Analyze the target Job Description and extract
    skills, technologies, keywords, expectations,
    and ATS terminology.
    """

    data = invoke_json(
        JD_ANALYSIS_PROMPT,
        {
            "job_description": state["job_description"]
        }
    )

    state["jd_analysis"] = JDAnalysis(**data)

    return state