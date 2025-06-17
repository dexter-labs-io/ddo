import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

from ddo_core.agent import Agent
from ddo_core.domain import Domain
from ddo_runtime.runtime import Runtime

def simple_logic(input_data):
    return f"Processed: {input_data}"

my_domain = Domain(logic=simple_logic)
my_agent = Agent(name="test-agent", domain=my_domain)
runtime = Runtime(agent=my_agent)
result = runtime.run("Hello DDO")

print(result)

