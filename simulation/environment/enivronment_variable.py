"""Contain base class for physical environment characteeristics."""
from abc import ABC, abstractmethod
from simulation.nodes import Node


class EnvironmentVariable(ABC):
    """
    Environment variable - changable environemnt properties.

    Class implements `Observer` pattern and notify all subscribed nodes, 
    that his value changed.

    :ivar `observers` - list of `Node` instances that observe this value
    """
    existing_variables = {}

    def __init__(self):
        """Add empty observer list to newly created environmental variable."""
        self.observers = []

    @property
    @abstractmethod
    def value(self):
        """Value of some Environment param."""
        raise NotImplementedError

    def notify_all(self) -> None:
        """Notify all tracking `Nodes`, about value change.

        When value of environment variable change in some way - it should
        tell all devices in simulation that tracks it, that such change event
        occured, so they can do some actions to handle it.
        This method doing that by calling notify method on every of his subsribers
        and passing there new it's value.
        """
        for node in self.observers:
            node.notify(self.value)

    def track(self, tracker: Node) -> None:
        """Add device that will track environment value to observers list."""
        self.observers.append(tracker)

    def __init_subclass__(cls):
        """Register all existing environment variables"""
        EnvironmentVariable.existing_variables[cls.__name__] = cls
    
