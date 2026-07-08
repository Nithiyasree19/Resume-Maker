from langchain_core.prompts import ChatPromptTemplate

SKILLS_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert technical resume writer.

Organize the candidate's technical skills based on relevance to the target job.

Rules:

- Prioritize skills that match the job description.
- Do not invent new skills.
- Keep only skills the candidate actually possesses.

Return ONLY a JSON array.

Example:

[
  "Python",
  "FastAPI",
  "SQL",
  "Git"
]
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