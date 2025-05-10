# core/tool_registry.py

import logging
from fastmcp.core.tool_manager import ToolManager
from fastmcp.tools.whatsapp_tool import WhatsAppMessenger
import os
from dotenv import load_dotenv

logger = logging.getLogger(__name__)


def initialize_tools():
    load_dotenv()
    manager = ToolManager()
    sid = os.getenv("TWILIO_SID")
    token = os.getenv("TWILIO_AUTH_TOKEN")
    from_wa = os.getenv("TWILIO_FROM")
    if not all([sid, token, from_wa]):
        logger.error("Missing Twilio environment variables.")
        raise RuntimeError("Missing Twilio environment variables.")
    whatsapp_tool = WhatsAppMessenger(
        account_sid=sid,
        auth_token=token,
        from_whatsapp=from_wa
    )
    manager.register_tool("whatsapp", whatsapp_tool)
    return manager
