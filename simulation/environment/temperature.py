"""Example implementation of `EnvironmentVariable`"""
from simulation.environment import EnvironmentVariable


class Temperature(EnvironmentVariable):
    def __init__(self, degrees: int = 20):
        super().__init__()
        self.__degrees = degrees

    @property
    def value(self):
        return self.__degrees

    @value.setter
    def value(self, val):
        self.__degrees = val
        self.notify_all()
