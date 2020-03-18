"""Contains description of `Tile` from which  `Surface` consists."""
from abc import ABC, abstractmethod
from typing import List, TypeVar, Dict
from enum import Enum, auto
from simulation.network import Frame
from simulation.nodes import Node
Content = TypeVar('Content', Frame, Node)


class TileType(Enum):
    """Type of created tile."""
    EMPTY = 0
    SLOT = 1
    WALL = 2


class TileState(Enum):
    """State of tile."""
    EMPTY = auto()
    NOT_EMPTY = auto()


class Tile:
    """Describes the most basic empty element  of `Surface`."""

    def __init__(self, tile_type: TileType):
        """
        On create all tiles are empty because they still hadn't received.
        nothing, and there no devices connected to them.
        :param tile_type: - type of `Tile`, describes it's logic. 
        """
        self.type = tile_type
        self.__state: TileState = TileState.EMPTY
        self.__content: Content = None
        self.neinghbors = []

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, val: Content):
        if self.__state is TileState.EMPTY:
            self.__state = TileState.NOT_EMPTY
            self.__content = val
        else:
            print("Collision !!!!")

    def propagate(self) -> None:
        """Propagate frame content on surface."""
        for tile in self.__neinghbors:
            tile.receive(self.content)
        self.__state = TileState.EMPTY

    def receive(self, val: Frame) -> None:
        """Receive a frame and set's it as a Tile content."""
        self.content = val
