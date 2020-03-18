"""Class describes surface on which frames are modving."""
from enum import Enum, auto
from typing import List, TypeVar, Dict
from simulation.network import Frame
# from simulation.nodes import Node

Content = TypeVar('Content', 'Frame', 'Node')


class TileType(Enum):
    """Type of created tile"""
    EMPTY = 0
    SLOT = 1
    WALL = 2


class State(Enum):
    """State of tile"""
    EMPTY = auto()
    NOT_EMPTY = auto()


class Tile:
    """Describes the most basic empty element  of `Surface`."""

    def __init__(self, type: TileType):
        """
        On create all tiles are empty because they still hadn't received 
        nothing, and there no devices connected to them.
        :param type: - type of element 
        """
        self.__state: State = State.EMPTY
        self.__content: Content = None
        self.neinghbors = []

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

    def propagate(self) -> None:
        """Propagate frame content on surface."""
        for tile in self.__neinghbors:
            tile.receive(self.content)
        self.__state = State.EMPTY

    def receive(self, val: Frame) -> None:
        """Receive a frame and set's it as a Tile content."""
        self.content = val


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

    def __init__(self, map: 'Some map content', row_width: int):
        self.enrty_points = self.from_map(map)

    def from_map(self, surface: List[int]) -> List[Tile]:
        """Generate graph and assign entry points from provided map.

        :param surface: - array from which map will be genereated
        :param row_width: - number of elements in map row
        :return: - list of tiles, where nodes could be placed
        """
        row_width = 6
        surface = [
            [2, 2, 2, 1, 0, 1],
            [2, 0, 0, 0, 0, 2],
            [2, 1, 2, 2, 2, 2]
        ]

        def extend_surface(surface: List[int]) -> None:
            """
            Extend surface,by placing wall tiles on bounds.

            Because lists are passed as reference, doesn't return anything
            """
            cols = len(surface[0])
            rows = len(surface)
            surface.insert(0, [TileType.WALL.value] * cols)
            surface.append([TileType.WALL.value]*cols)

            def extend_row(row):
                row.insert(0, TileType.WALL.value)
                row.append(TileType.WALL.value)
            map(extend_row, surface)

        def map_row(self, element):
            """Function to perform mapping."""
            tile = Tile(TileType(element))
            if TileType(element) is TileType.SLOT:
                self.entry_points.append(tile)
            return tile
        surface = [map(map_row, row) for row in surface]

        for i, row in enumerate(surface[1:-1]):
            for j, tile in enumerate(row[1:-1]):
                up = surface[i-1][j]
                bottom = surface[i+1][j]
                left = surface[i][j-1]
                right = surface[i][j+1]
                tile.neignhbors = [up, bottom, left, right]
        return enrty_points
