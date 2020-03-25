"""Desribes classes used for `Node` communication."""
from simulation.network import Surface
from simulation.network import Frame
from simulation.nodes import Node
from typing import List


class Network:
    """Describes medium where all communication happend."""

    def __init__(self, map: List[List[int]]):
        self._free_slots = []
        self._radio_channels = {
            '1000': Surface(map),
            '1220': Surface(map)
        }
        # tmp demonstration of how it should work.
        # device identifier and device entry point index.
        self._device_entry_points = {
            'device1': 0
        }

    def register_node(self, node: Node, slot: int):
        """
        Add node to network, so it can start share messages.
        :param `node`: - that represents this node.
        :param `slot`: - id of slot on surface, where this node will be assigned
        """
        print(f"Device was succesfully registered on slot {slot}")

    def transmit(self, frame: Frame):
        """Sends frame given as argument."""
        print(f"Transmitting frame: {str(frame)}")
