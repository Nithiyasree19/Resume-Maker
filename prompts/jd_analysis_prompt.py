from langchain_core.prompts import ChatPromptTemplate

JD_ANALYSIS_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert ATS Job Description Analyzer.

Analyze the provided Job Description and extract:

1. Required Skills
2. Preferred Technologies
3. Domain Keywords
4. Role Expectations
5. ATS Keywords

Return ONLY valid JSON using this structure:

{{
  "required_skills": [],
  "preferred_technologies": [],
  "domain_keywords": [],
  "role_expectations": [],
  "ats_keywords": []
}}

Do not include explanations.
Do not add markdown.
Do not wrap the JSON in code blocks.
"""
        ),
        (
            "human",
            """
Job Description:

{job_description}
"""
        )
    ]
)