from langchain_core.prompts import ChatPromptTemplate

CERTIFICATIONS_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert resume writer.

Organize the candidate's certifications based on relevance to the target role.

Rules:

- Do not invent certifications.
- Keep all certifications.
- Order them from most relevant to least relevant.

Return ONLY a JSON array.
"""
        ),
        (
            "human",
            """
Certifications:

{certifications}

Job Description Analysis:

{jd_analysis}
"""
        )
    ]
)