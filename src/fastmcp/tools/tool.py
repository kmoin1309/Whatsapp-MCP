from fastmcp.tools.whatsapp_tool import WhatsAppMessenger

tool = WhatsAppMessenger(
    account_sid="YOUR_TWILIO_SID",
    auth_token="YOUR_TWILIO_AUTH_TOKEN",
    from_whatsapp="YOUR_TWILIO_WHATSAPP_NUMBER"
)
tool_manager.register(tool)
