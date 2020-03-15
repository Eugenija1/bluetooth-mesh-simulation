"""Class describes surface on which frames are modving."""
from enum import Enum, auto
from typing import List, TypeVar, Dict
from simulation.network import Frame
from simulation.nodes import Node

Content = TypeVar('Content', Frame, Node)


class State(Enum):
    EMPTY = auto()
    NOT_EMPTY = auto()


class Surface:
    """
    Contain graph of tiles.

    Surface creates graph of tiles from provided map and marks there entry points.

        Purposes:
            Each frequency will contain a surface.
            Packets sent by this frequency will run across this surface. 
            In case of colisions, there will be an error on the surface that
            will inform the network about it.
    """

    def __init__(self, map: 'Some map content'):
        self.enrty_points = self.from_map(map)

    def from_map(self, map) -> Dict[str, Node]:
        """Generate graph and assign entry points from provided map."""
        enrty_points = {}
        # some code here
        return enrty_points


class Tile:
    """Describes the most basic empty element  of `Surface`."""

    def __init__(self):
        """
        On create all tiles are empty because they still hadn't received 
        nothing, and there no devices connected to them.
        """
        self.__state: State = State.EMPTY
        self.__content: Content = None

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, val: Content):
        if self.__state is State.EMPTY:
            self.__state = State.NOT_EMPTY
            self.__content = val
        else:
            print("Collision !!!!")

    def propagate(self, targets: List[Tile]) -> None:
        """Propagate frame content on surface."""
        for target in targets:
            target.receive(self.content)
        self.__state = State.EMPTY

    def receive(self, val: Frame) -> None:
        """Receive a frame and set's it as a Tile content."""
        self.content = val
