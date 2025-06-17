# tool.py
# Defines a generic Tool wrapper with an execution method

class Tool:
    def __init__(self, name, function):
        self.name = name
        self.function = function  # function should be a callable

    def execute(self, *args, **kwargs):
        # Calls the tool's function with given arguments
        return self.function(*args, **kwargs)
