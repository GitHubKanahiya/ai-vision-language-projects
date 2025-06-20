
class BaseAgent:
    def __init__(self, name):
        self.name = name

    def run(self, input_data, memory, topic):
        raise NotImplementedError("Each agent must implement its own run() method.")
