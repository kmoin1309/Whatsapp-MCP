# agents/base_agent.py

class BaseAgent:
    def __init__(self, name):
        self.name = name

    def act(self, input_data):
        raise NotImplementedError("Each agent must implement the act method.")
