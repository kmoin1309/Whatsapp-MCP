# src/fastmcp/tools/whatsapp_tool.py

import logging
from twilio.rest import Client
from fastmcp.tools.tool import Tool
from typing import Dict, Any

logger = logging.getLogger(__name__)


class WhatsAppMessenger(Tool):
    """
    Tool to send WhatsApp messages using Twilio API.
    """
    name = "whatsapp_messenger"
    description = "Send WhatsApp messages using Twilio"

    def __init__(self, account_sid: str, auth_token: str, from_whatsapp: str):
        super().__init__()
        if not all([account_sid, auth_token, from_whatsapp]):
            raise ValueError(
                "Twilio credentials and WhatsApp sender number must be provided.")
        self.client = Client(account_sid, auth_token)
        self.from_whatsapp = from_whatsapp

    def run(self, to: str, message: str) -> Dict[str, Any]:
        """
        Send a WhatsApp message.

        Args:
            to (str): Recipient's WhatsApp number (in E.164 format, e.g., '+12345556789').
            message (str): Message body.

        Returns:
            dict: Status and message SID or error.
        """
        if not to or not message:
            logger.error("Recipient and message must be provided.")
            return {"status": "error", "error": "Recipient and message must be provided."}
        if not to.startswith('+'):
            logger.error(
                "Recipient number must be in E.164 format (start with '+').")
            return {"status": "error", "error": "Recipient number must be in E.164 format (start with '+')."}
        try:
            msg = self.client.messages.create(
                body=message,
                from_=f'whatsapp:{self.from_whatsapp}',
                to=f'whatsapp:{to}'
            )
            logger.info(f"WhatsApp message sent: SID={msg.sid}")
            return {"status": "success", "sid": msg.sid}
        except Exception as e:
            logger.error(f"Failed to send WhatsApp message: {e}")
            return {"status": "error", "error": str(e)}
