from langchain_core.prompts import ChatPromptTemplate

PROJECTS_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert technical resume writer.

Rewrite the candidate's projects.

Rules:

- Select the projects most relevant to the target role.
- Highlight technologies actually used.
- Do not fabricate features or technologies.
- Improve clarity and ATS relevance.

Return ONLY a JSON.

Output format:

[
  "Project 1 : rewritten description",
  "Project 2 : rewritten description"
]"""
        ),(
            "human",
            """
Projects:

{projects}

Job Description Analysis:

{jd_analysis}
"""
        )
    ]
)