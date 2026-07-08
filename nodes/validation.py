from state import ResumeState


def validate_inputs(state: ResumeState) -> ResumeState:
    """
    Validate the candidate information and job description.
    Ensures all mandatory fields are present before the workflow proceeds.
    """

    candidate = state["candidate"]
    job_description = state["job_description"]

    # Validate job description
    if not job_description or not job_description.strip():
        raise ValueError("Job Description is required.")

    # Validate candidate fields
    required_fields = [
        "name",
        "email",
        "phone",
        "education",
        "current_role",
        "years_of_experience",
        "skills",
        "experience",
        "projects",
        "certifications",
    ]

    for field in required_fields:
        value = getattr(candidate, field)

        if value is None:
            raise ValueError(f"Candidate field '{field}' is missing.")

        if isinstance(value, str) and not value.strip():
            raise ValueError(f"Candidate field '{field}' cannot be empty.")

        if isinstance(value, list) and len(value) == 0:
            raise ValueError(f"Candidate field '{field}' cannot be empty.")

    return state