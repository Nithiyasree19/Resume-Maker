from langchain_core.prompts import ChatPromptTemplate

SUMMARY_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert resume writer.

Generate a professional summary that:

- Aligns with the target job description.
- Highlights the candidate's most relevant skills and experience.
- Uses ATS-friendly terminology.
- Is professional and concise (3–5 sentences).
- Does NOT invent skills, experience, or achievements.

Return only the professional summary.
"""
        ),
        (
            "human",
            """
Candidate Analysis:

{candidate_analysis}

Job Description Analysis:

{jd_analysis}
"""
        )
    ]
)