from .base import call_llm, log_response, get_current_session

def run(username: str, career_goal: str):
    prompt = f"Conduct a mock behavioral interview for a candidate aiming to be a {career_goal}."
    mock = call_llm(prompt)
    session = get_current_session(username)
    log_response(username, "Interview Coach", session, mock)
    return mock
