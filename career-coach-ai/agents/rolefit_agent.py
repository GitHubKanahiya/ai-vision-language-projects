from .base import call_llm, log_response, get_current_session

def run(username: str, resume_text: str, role_description: str):
    prompt = f"Assess how well this resume fits the role:\n\nResume:\n{resume_text}\n\nRole:\n{role_description}"
    analysis = call_llm(prompt)
    session = get_current_session(username)
    log_response(username, "Role-Fit Analyzer", session, analysis)
    return analysis
