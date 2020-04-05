from abc import ABC, abstractmethod


class Element(ABC):
    @abstractmethod
    def notify(self, environment_variable_value):
        pass
