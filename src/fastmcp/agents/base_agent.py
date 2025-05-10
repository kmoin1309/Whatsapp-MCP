# agents/base_agent.py

from typing import Any, Dict


class BaseAgent:
    """
    Base class for all agents.
    """

    def __init__(self, name: str):
        self.name = name

    def act(self, input_data: Dict[str, Any]) -> Any:
        """
        Perform an action with the given input data.
        """
        raise NotImplementedError("Each agent must implement the act method.")
