# cli/main.py

import argparse
from fastmcp.tools.whatsapp_tool import WhatsAppMessenger
from fastmcp.core.tool_manager import ToolManager
import os
from dotenv import load_dotenv


def send_whatsapp_message():
    load_dotenv()

    tool = WhatsAppMessenger(
        account_sid=os.getenv("TWILIO_SID"),
        auth_token=os.getenv("TWILIO_AUTH_TOKEN"),
        from_whatsapp=os.getenv("TWILIO_FROM")
    )

    recipient = input("Enter recipient number (with +countrycode): ")
    message = input("Enter message: ")
    result = tool.run(to=recipient, message=message)
    if result.get("status") == "success":
        print(f"Message sent. SID: {result['sid']}")
    else:
        print(f"Error: {result.get('error')}")


def list_tools():
    manager = ToolManager()
    print("Available tools:")
    for name in manager.list_tools():
        print(f"- {name}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="FastMCP CLI")
    parser.add_argument("--send-whatsapp", action="store_true",
                        help="Send WhatsApp message")
    parser.add_argument("--list-tools", action="store_true",
                        help="List available tools")
    args = parser.parse_args()

    if args.send_whatsapp:
        send_whatsapp_message()
    elif args.list_tools:
        list_tools()
    else:
        print("No command specified. Use --help for options.")
