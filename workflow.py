from langgraph.graph import StateGraph, END

from state import ResumeState

from nodes.validation import validate_inputs
from nodes.jd_analysis import analyze_jd
from nodes.candidate_analysis import analyze_candidate
from nodes.professional_summary import generate_professional_summary
from nodes.skills import optimize_skills
from nodes.experience import enhance_experience
from nodes.projects import generate_projects
from nodes.certifications import organize_certifications
from nodes.resume_assembly import assemble_resume


workflow = StateGraph(ResumeState)

# Add Nodes
workflow.add_node("validate_inputs", validate_inputs)
workflow.add_node("analyze_jd", analyze_jd)
workflow.add_node("analyze_candidate", analyze_candidate)
workflow.add_node("generate_professional_summary", generate_professional_summary)
workflow.add_node("optimize_skills", optimize_skills)
workflow.add_node("enhance_experience", enhance_experience)
workflow.add_node("generate_projects", generate_projects)
workflow.add_node("organize_certifications", organize_certifications)
workflow.add_node("assemble_resume", assemble_resume)

# Entry Point
workflow.set_entry_point("validate_inputs")

# Edges
workflow.add_edge("validate_inputs", "analyze_jd")
workflow.add_edge("analyze_jd", "analyze_candidate")
workflow.add_edge("analyze_candidate", "generate_professional_summary")
workflow.add_edge("generate_professional_summary", "optimize_skills")
workflow.add_edge("optimize_skills", "enhance_experience")
workflow.add_edge("enhance_experience", "generate_projects")
workflow.add_edge("generate_projects", "organize_certifications")
workflow.add_edge("organize_certifications", "assemble_resume")
workflow.add_edge("assemble_resume", END)

graph = workflow.compile()