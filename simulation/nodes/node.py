"""Contains abstract base for all nodes"""
from simulation.network import Frame


class Node:
    """Device/collection of devices, that could communicate via network."""

    count = 0

    def __init__(self):
        self.id = self.set_id()

    def receive(self, frame: Frame):
        """Receives frame passed to device."""
        pass

    def set_id(self):
        return Node.count + 1
