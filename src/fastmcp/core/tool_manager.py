# core/tool_manager.py

from fastmcp.tools.tool import Tool


class ToolManager:
    def __init__(self):
        self.tools = {}

    def register_tool(self, name: str, tool: Tool):
        self.tools[name] = tool

    def get_tool(self, name: str):
        return self.tools.get(name)

    def list_tools(self):
        return list(self.tools.keys())
