from .base import call_llm, log_response, get_current_session

def run(username: str, resume_text: str, job_goal: str):
    prompt = f"Optimize this resume for the job goal '{job_goal}':\n\n{resume_text}"
    feedback = call_llm(prompt)
    session = get_current_session(username)
    log_response(username, "Resume Optimizer", session, feedback)
    return feedback
