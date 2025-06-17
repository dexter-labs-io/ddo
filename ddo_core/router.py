# router.py
# ToolRouter class dynamically dispatches tool calls based on name

class ToolRouter:
    def __init__(self, tools):
        self.tools = {tool.name: tool for tool in tools}  # tool name mapping

    def route(self, tool_name, *args, **kwargs):
        # Routes the request to the correct tool based on name
        if tool_name in self.tools:
            return self.tools[tool_name].execute(*args, **kwargs)
        raise ValueError(f"Tool '{tool_name}' not found")
