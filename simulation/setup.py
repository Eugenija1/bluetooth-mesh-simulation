from simulation.physical_objects import *
from simulation.network import Surface, Frame, Network
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
    network = Network(surface)
    print("Surface looks like")
    for row in network.radio_channels['1000'].surface:
        print(row)
    network.send('1000', 'device1', Frame(source_id=1, dest_id=1))
    # surface.entry_points[0].content = Frame(1, 1)
    # surface.entry_points[0].propagate()


if __name__ == "__main__":
    run()
