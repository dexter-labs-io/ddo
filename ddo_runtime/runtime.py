# runtime.py
# The Runtime executes an agent and provides an entrypoint for interaction

from ddo_core.agent import Agent

class Runtime:
    def __init__(self, agent: Agent):
        self.agent = agent

    def run(self, input_data):
        # Executes the agent’s logic on given input
        return self.agent.act(input_data)
