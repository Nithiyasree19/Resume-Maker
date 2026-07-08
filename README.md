# Resume Maker Workflow using LangChain

## Overview

Resume Maker is a modular AI-powered application that generates a job-specific resume based on a candidate's profile and a target Job Description (JD).

The system analyzes the job description, compares it with the candidate's information, and generates ATS-friendly resume content while preserving factual accuracy.

The workflow is implemented using **LangGraph** as a deterministic pipeline without using autonomous agents.

---

## Objective

The objective of this project is to build a modular Resume Maker workflow that:

* Accepts candidate information
* Accepts a target Job Description
* Analyzes the requirements of the job
* Identifies relevant candidate skills and experience
* Generates optimized resume content
* Produces structured output suitable for PDF/DOCX generation and ATS pipelines

---

## Features

* Candidate Information Validation
* Job Description Analysis
* Candidate Profile Analysis
* Professional Summary Generation
* Technical Skills Optimization
* Professional Experience Enhancement
* Project Selection and Rewriting
* Certification Prioritization
* Structured Resume Generation
* Deterministic LangGraph Workflow
* Modular Node-Based Architecture

---

## Technology Stack

* Python 3.11+
* LangChain
* LangGraph
* Google Gemini API
* Pydantic
* python-dotenv

---

## Project Structure

```
resume-maker/
│
├── app.py
├── workflow.py
├── config.py
├── state.py
├── requirements.txt
├── .env
│
├── models/
├── nodes/
├── prompts/
├── utils/
└── sample_data/
```

---

## Workflow

```
Input Validation
        │
        ▼
JD Analysis
        │
        ▼
Candidate Profile Analysis
        │
        ▼
Professional Summary Generation
        │
        ▼
Skills Optimization
        │
        ▼
Experience Enhancement
        │
        ▼
Projects Generation
        │
        ▼
Certifications Organization
        │
        ▼
Final Resume Assembly
```

---

## Input

### Candidate Information

* Name
* Email
* Phone
* Education
* Current Role
* Years of Experience
* Skills
* Experience
* Projects
* Certifications

### Job Description

A plain text Job Description (JD) containing:

* Required Skills
* Preferred Technologies
* Responsibilities
* Role Expectations

---

## Output

The workflow generates a structured resume containing:

* Profile
* Professional Summary
* Technical Skills
* Professional Experience
* Projects
* Certifications

The output can be easily integrated with:

* PDF generators
* DOCX generators
* Resume templates
* ATS optimization pipelines

---

## Future Scope

The architecture is designed to support future integration with:

* Model Context Protocol (MCP)
* ChatGPT as an external client
* Other LLM-based applications
* PDF generation
* DOCX generation
* Resume templates
* Web API integration

---

## Author

Nithiyasree M
