from langchain_core.prompts import ChatPromptTemplate

EXPERIENCE_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert resume writer.

Rewrite the candidate's experience.

Rules:

- Preserve factual accuracy.
- Do NOT invent achievements.
- Use ATS-friendly technical terminology.
- Improve readability.
- Use concise bullet-style statements.

Return ONLY a JSON array.
"""
        ),
        (
            "human",
            """
Experience:

{experience}

Job Description Analysis:

{jd_analysis}
"""
        )
    ]
)