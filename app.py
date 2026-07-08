import json

from models.candidate import Candidate
from workflow import graph

# Load Candidate Data
with open("sample_data/candidate.json", "r") as file:
    candidate_data = json.load(file)

candidate = Candidate(**candidate_data)

# Load Job Description
with open("sample_data/jd.txt", "r") as file:
    job_description = file.read()

# Initial Workflow State
state = {
    "candidate": candidate,
    "job_description": job_description,
}

# Run Workflow
result = graph.invoke(state)

# Print Final Resume
print(result["resume"].model_dump_json(indent=4))