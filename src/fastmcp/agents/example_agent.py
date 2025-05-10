# agents/example_agent.py

from fastmcp.agents.base_agent import BaseAgent
from fastmcp.tools.whatsapp_tool import WhatsAppMessenger
import os
from dotenv import load_dotenv
from typing import Dict, Any


class ExampleAgent(BaseAgent):
    def __init__(self, name: str):
        super().__init__(name)
        load_dotenv()
        self.whatsapp = WhatsAppMessenger(
            account_sid=os.getenv("TWILIO_SID"),
            auth_token=os.getenv("TWILIO_AUTH_TOKEN"),
            from_whatsapp=os.getenv("TWILIO_FROM")
        )

    def act(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        input_data should be a dict with keys:
        - to: target number (e.g., +918766996609)
        - message: string

        Returns:
            dict: WhatsApp sending result.
        """
        to = input_data.get("to")
        message = input_data.get("message")

        if not to or not message:
            raise ValueError("Missing 'to' or 'message' in input_data")

        return self.whatsapp.run(to=to, message=message)
