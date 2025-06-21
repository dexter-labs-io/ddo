# ddo/core/memory_manager.py

class MemoryManager:
    """
    In-memory context storage (per-agent).
    Replace with Redis later.
    """

    def __init__(self):
        self.memory_store = {}

    def retrieve_context(self, agent_id: str) -> dict:
        return self.memory_store.get(agent_id, {})

    def store_context(self, agent_id: str, prompt: str, result: any):
        self.memory_store[agent_id] = {
            "last_prompt": prompt,
            "last_result": result
        }
