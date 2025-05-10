# cli/agent_cli.py

import argparse
from fastmcp.agents.example_agent import ExampleAgent


def run_example_agent():
    agent = ExampleAgent("WhatsAppAgent")
    recipient = input("Enter recipient number (with +countrycode): ")
    message = input("Enter message: ")
    result = agent.act({"to": recipient, "message": message})
    if isinstance(result, dict) and result.get("status") == "success":
        print(f"Message sent. SID: {result['sid']}")
    else:
        print(
            f"Error: {result.get('error') if isinstance(result, dict) else result}")


def main():
    parser = argparse.ArgumentParser(description="Agent CLI for FastMCP")
    parser.add_argument("--use-agent", action="store_true",
                        help="Run example agent to send WhatsApp message")
    args = parser.parse_args()

    if args.use_agent:
        run_example_agent()
    else:
        print("No agent command specified. Use --help for options.")


if __name__ == "__main__":
    main()
