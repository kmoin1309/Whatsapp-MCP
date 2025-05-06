# src/fastmcp/tools/whatsapp_tool.py

from twilio.rest import Client
from fastmcp.tools.tool import Tool


class WhatsAppMessenger(Tool):
    name = "whatsapp_messenger"
    description = "Send WhatsApp messages using Twilio"

    def __init__(self, account_sid: str, auth_token: str, from_whatsapp: str):
        self.client = Client(account_sid, auth_token)
        self.from_whatsapp = from_whatsapp

    def run(self, to: str, message: str):
        return self.client.messages.create(
            body=message,
            from_=f'whatsapp:{self.from_whatsapp}',
            to=f'whatsapp:{to}'
        ).sid
