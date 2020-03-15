"""Desribes classes used for `Node` communication."""
from simulation.physical_objects import Surface


class Network:
    """Describes medium where all communication happend."""

    def __init__(self, map: 'Some format of map'):
        self.radio_channels = {
            '1000': Surface(map),
            '1220': Surface(map)
        }
