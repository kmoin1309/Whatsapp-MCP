# core/tool_manager.py

from fastmcp.tools.tool import Tool
from typing import Dict, List, Optional


class ToolManager:
    """
    Manages registration and retrieval of tools.
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ToolManager, cls).__new__(cls)
            cls._instance.tools = {}
        return cls._instance

    def register_tool(self, name: str, tool: Tool) -> None:
        self.tools[name] = tool

    def get_tool(self, name: str) -> Optional[Tool]:
        return self.tools.get(name)

    def list_tools(self) -> List[str]:
        return list(self.tools.keys())
