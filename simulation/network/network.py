"""Desribes classes used for `Node` communication."""
from simulation.network import Surface
from simulation.network import Frame
from simulation.nodes import Node
from typing import List


class Network:
    """Describes medium where all communication happend."""

    def __init__(self, map: List[List[int]]):
        self.free_slots = []
        self.radio_channels = {
            '1000': Surface(map),
            '1220': Surface(map)
        }
        # tmp demonstration of how it should work.
        # device identifier and device entry point index.
        self.device_entry_points = {
            'device1': 0
        }

    def send(self, frequency: str, device: str, frame: Frame):
        """
        Start frame propagation on surface on given frequency.
        :param  `frequency`: - frequency on whic message will be propagated
        :param  `device`: - device from which frame will be sent
        :param  `frame`: - frame that should be transmitted
        """
        entry_point = self.device_entry_points[device]
        radio_channel = self.radio_channels[frequency]
        # tmp method, will be replaced
        radio_channel.entry_points[entry_point].content = frame
        # 
        radio_channel.entry_points[entry_point].propagate()

    def add_node(self, frequency: int, slot: int, node: 'Node'):
        """
        Add node to network so it can start share messages on `frequency`
        :param `frequency`: - freqency, on which this node will listen and send
        :param `slot`: - id of slot on surface, where this node will be assigned
        :param `node`: - object, that represents this node.
        """
        pass
