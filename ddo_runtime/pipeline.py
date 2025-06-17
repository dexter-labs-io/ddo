# pipeline.py
# Defines a simple data pipeline composed of ordered steps (functions)

class Pipeline:
    def __init__(self, steps):
        self.steps = steps  # List of callables

    def execute(self, input_data):
        # Executes all steps sequentially on the input
        data = input_data
        for step in self.steps:
            data = step(data)
        return data
