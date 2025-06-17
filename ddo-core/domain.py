# domain.py
# Defines a Domain abstraction that handles specific logic for an agent

class Domain:
    def __init__(self, logic):
        self.logic = logic  # logic is a callable that processes input

    def handle(self, input_data):
        # Executes domain-specific logic
        return self.logic(input_data)
