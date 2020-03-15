"""Contains abstract base for all nodes"""
from simulation.network import Frame
class Node:
    """Device/collection of devices, that could communicate via network."""

    def receive(self, frame: Frame):
        """Receives frame passed to device."""
        pass
