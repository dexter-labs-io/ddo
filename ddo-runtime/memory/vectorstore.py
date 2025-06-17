# vectorstore.py
# In-memory store for key-vector mappings, useful for embedding-based memory

class VectorStoreMemory:
    def __init__(self):
        self.vectors = {}

    def store(self, key, vector):
        # Stores a vector under a key
        self.vectors[key] = vector

    def retrieve(self, key):
        # Retrieves a stored vector
        return self.vectors.get(key, None)
