from state import ResumeState

from models.candidate_analysis import CandidateAnalysis

from prompts.candidate_analysis_prompt import CANDIDATE_ANALYSIS_PROMPT

from utils.llm_helper import invoke_json


def analyze_candidate(state: ResumeState) -> ResumeState:
    """
    Analyze the candidate profile against the
    Job Description analysis.
    """

    candidate = state["candidate"]

    data = invoke_json(
        CANDIDATE_ANALYSIS_PROMPT,
        {
            "candidate": candidate.model_dump_json(indent=2),
            "jd_analysis": state["jd_analysis"].model_dump_json(indent=2),
        },
    )

    state["candidate_analysis"] = CandidateAnalysis(**data)

    return state