"""Decribe messages that are passing through network."""
from dataclasses import dataclass


@dataclass
class Frame:
    """Describe frame, that devices sen to each other."""

    source_id: int
    dest_id: int
