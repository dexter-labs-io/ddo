# ddo/core/orchestrator.py

from core.planner import Planner
from core.executor import Executor
from core.memory_manager import MemoryManager

class DDOOrchestrator:
    """
    Main orchestrator class.
    Responsible for managing THINK → PLAN → ACT loop.
    """

    def __init__(self, agent_id="default"):
        self.agent_id = agent_id
        self.planner = Planner()
        self.executor = Executor()
        self.memory = MemoryManager()

    def run(self, prompt: str) -> dict:
        """
        Executes a prompt via THINK → PLAN → ACT.
        Returns structured response dict.
        """

        # Retrieve context from memory
        context = self.memory.retrieve_context(self.agent_id)

        try:
            # PLAN: Create execution plan
            plan = self.planner.generate_plan(prompt, context)

            # ACT: Execute the plan
            result = self.executor.execute_plan(plan)

            # Store memory
            self.memory.store_context(self.agent_id, prompt, result)

            return {
                "status": "success",
                "plan": plan,
                "result": result
            }

        except Exception as e:
            # Failsafe error handling
            return {
                "status": "error",
                "error": str(e)
            }
