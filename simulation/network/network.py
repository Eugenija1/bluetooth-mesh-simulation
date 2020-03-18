"""Desribes classes used for `Node` communication."""
from simulation.network import Surface
from simulation.nodes import Node

class Network:
    """Describes medium where all communication happend."""

    def __init__(self, map: 'Some format of map'):
        self.free_slots = []
        self.radio_channels = {
            '1000': Surface(map),
            '1220': Surface(map)
        }

    def add_node(self, frequency: int, slot: int, node: 'Node'):
        """
        Add node to network so it can start share messages on `frequency` 
        :param `frequency`: - freqency, on which this node will listen and send
        :param `slot`: - id of slot on surface, where this node will be assigned
        :param `node`: - object, that represents this node. 
        """
        pass
