"""Desribes classes used for `Node` communication."""
from dataclasses import dataclass


class Network:
    """Describes medium where all communication happend."""

    def __init__(self):
        self.channels = {
            '1000': [],
            '1220': []
        }


@dataclass
class Frame:
    """Describe frame, that devices sen to each other."""
    source_id: int
    dest_id: int
