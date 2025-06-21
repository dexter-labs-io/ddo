# ddo/core/executor.py

from plugins.tools.echo_tool import echo_tool
from plugins.tools.search_tool import search_tool

class Executor:
    """
    Executes a list of steps as defined in a plan.
    Each step should contain 'tool' and 'input'.
    """

    TOOL_MAP = {
        "echo": echo_tool,
        "search": search_tool
    }

    def execute_plan(self, plan: list) -> list:
        results = []

        for step in plan:
            tool_name = step.get("tool")
            input_data = step.get("input")

            tool_fn = self.TOOL_MAP.get(tool_name)

            if not tool_fn:
                results.append({
                    "tool": tool_name,
                    "error": f"Unknown tool: {tool_name}"
                })
                continue

            try:
                output = tool_fn(input_data)
                results.append({
                    "tool": tool_name,
                    "output": output
                })
            except Exception as e:
                results.append({
                    "tool": tool_name,
                    "error": str(e)
                })

        return results
