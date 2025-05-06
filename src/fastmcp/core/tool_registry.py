# core/tool_registry.py

from fastmcp.core.tool_manager import ToolManager
from fastmcp.tools.whatsapp_tool import WhatsAppMessenger
import os
from dotenv import load_dotenv


def initialize_tools():
    load_dotenv()
    manager = ToolManager()
    whatsapp_tool = WhatsAppMessenger(
        account_sid=os.getenv("TWILIO_SID"),
        auth_token=os.getenv("TWILIO_AUTH_TOKEN"),
        from_whatsapp=os.getenv("TWILIO_FROM")
    )
    manager.register_tool("whatsapp", whatsapp_tool)
    return manager
