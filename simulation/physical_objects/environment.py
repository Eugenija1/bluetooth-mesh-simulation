from simulation.environment import EnvironmentVariable


class Environment:
    def __init__(self):
        self.bake()

    def bake(self):
        """Create all variables that have classes and adds it to `variables` dict."""
        self.variables = {}
        for env_variable, var_creator in EnvironmentVariable.existing_variables.items():
            self.variables[env_variable] = var_creator()
