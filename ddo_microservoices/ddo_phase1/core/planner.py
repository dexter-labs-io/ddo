# ddo/core/planner.py

class Planner:
    """
    Naive planner to generate a linear plan (list of tool calls).
    """

    def generate_plan(self, prompt: str, context: dict) -> list:
        """
        Mock implementation: return a fixed one-step plan.
        """

        # TODO: Add LLM-based planner in future
        if "search" in prompt.lower():
            return [{"tool": "search", "input": prompt}]
        else:
            return [{"tool": "echo", "input": prompt}]
