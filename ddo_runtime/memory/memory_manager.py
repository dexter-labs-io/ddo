# memory_manager.py
# A generic wrapper to manage memory backends (e.g., vector, redis, filecache)

class MemoryManager:
    def __init__(self, backend):
        self.backend = backend  # backend should implement store() and retrieve()

    def get(self, key):
        # Retrieves a value from memory
        return self.backend.retrieve(key)

    def set(self, key, value):
        # Stores a value in memory
        return self.backend.store(key, value)
