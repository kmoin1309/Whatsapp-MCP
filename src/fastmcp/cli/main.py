# cli/main.py

import argparse
from fastmcp.tools.whatsapp_tool import WhatsAppMessenger
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
    sid = tool.run(to=recipient, message=message)
    print(f"Message sent. SID: {sid}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="FastMCP CLI")
    parser.add_argument("--send-whatsapp", action="store_true",
                        help="Send WhatsApp message")
    args = parser.parse_args()

    if args.send_whatsapp:
        send_whatsapp_message()
    else:
        print("No command specified. Use --help for options.")
