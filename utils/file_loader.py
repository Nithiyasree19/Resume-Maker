import json


def load_candidate(file_path: str) -> dict:
    """Load candidate information from a JSON file."""
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def load_job_description(file_path: str) -> str:
    """Load the job description from a text file."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read().strip()