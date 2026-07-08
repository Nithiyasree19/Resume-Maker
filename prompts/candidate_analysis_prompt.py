from langchain_core.prompts import ChatPromptTemplate

CANDIDATE_ANALYSIS_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert resume analyzer.

Compare the candidate profile with the Job Description.

Identify:

1. Matching Skills
2. Relevant Experience
3. Relevant Projects
4. Relevant Certifications

Return ONLY valid JSON.

{{
  "matching_skills": [],
  "relevant_experience": [],
  "relevant_projects": [],
  "relevant_certifications": []
}}

Do not invent information.

Only use facts present in the candidate profile.
"""
        ),
        (
            "human",
            """
Candidate:

{candidate}

JD Analysis:

{jd_analysis}
"""
        )
    ]
)