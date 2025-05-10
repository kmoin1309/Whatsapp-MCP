from abc import ABC, abstractmethod
from fastmcp.tools.whatsapp_tool import WhatsAppMessenger


class Tool(ABC):
    """
    Abstract base class for all tools.
    """
    name: str
    description: str

    @abstractmethod
    def run(self, *args, **kwargs):
        """
        Run the tool with the given arguments.
        """
        pass


tool = WhatsAppMessenger(
    account_sid="YOUR_TWILIO_SID",
    auth_token="YOUR_TWILIO_AUTH_TOKEN",
    from_whatsapp="YOUR_TWILIO_WHATSAPP_NUMBER"
)
tool_manager.register(tool)
