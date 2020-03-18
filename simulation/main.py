from simulation.physical_objects import *
from simulation.network import Surface, Frame
from simulation.environment import *
from simulation.nodes import *
from simulation.roles import *
from simulation.tabs import *

def run():
    surface = [
        [2, 2, 2, 1, 0, 1],
        [2, 0, 0, 0, 0, 2],
        [2, 1, 2, 2, 2, 2]
    ]

    surface = Surface(surface)
    print("Surface representation")
    for row in surface.surface:
        print(row)
    surface.entry_points[0].content = Frame(1, 1)
    surface.entry_points[0].propagate()

if __name__ == "__main__":
    run() 