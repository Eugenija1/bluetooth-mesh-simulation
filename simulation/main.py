from simulation.physical_objects import *
from simulation.network import Surface
from simulation.environment import *
from simulation.nodes import *
from simulation.roles import *
from simulation.tabs import *

if __name__ == '__main__':
    surface = [
        [2, 2, 2, 1, 0, 1],
        [2, 0, 0, 0, 0, 2],
        [2, 1, 2, 2, 2, 2]
    ]

    surface = Surface(surface)
    print(surface.enrty_points)
