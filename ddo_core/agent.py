# agent.py
# Defines the Agent class which uses a domain to act upon input

class Agent:
    def __init__(self, name, domain):
        self.name = name
        self.domain = domain  # A domain encapsulates the logic or context

    def act(self, input_data):
        # Delegates the handling of input to the domain logic
        return self.domain.handle(input_data)
