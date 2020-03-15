"""Base class for each role."""
from abc import ABC, abstractmethod


class Role(ABC):
    """
    Role - is a software-described behaviour for some device. 

    Each implementation of `Role` should have a described sequence of actions 
    they should perform in order to complete their taks.

    Every `Role` instance should be assigned to `Node`, that will perform it

    :ivar `node` - `Node` that perform this action.
    """

    def __init__(self, node):
        self.node = node

    @abstractmethod
    def perform(self):
        """Method starts a sequence of actions, that this role should do."""
        raise NotImplementedError
