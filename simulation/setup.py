from simulation.environment import *
from simulation.network import *
from simulation.nodes import *
from simulation.tabs import *

def run():
    surface = [
        [2, 2, 2, 1, 0, 1],
        [2, 0, 0, 0, 0, 2],
        [2, 1, 2, 2, 2, 2]
    ]
    network = Network(surface)
    print("Surface looks like")
    for row in network._radio_channels['1000'].surface:
        print(row)

    frame = Frame(source_id=1, dest_id=1)
    network.transmit(frame)



if __name__ == "__main__":
    run()
