from simulation.network import Network, Frame
from typing import List


class Simulation:
    def __init__(self, surface):
        self._network = surface

    def set_slot(self, slot_id, elements: List[Element]):
        node = Node(elements)
        self._network.register_node(node, slot_id) 
        return self._network

def run(surface):
    network = Network(surface)
    environment = Environment()
    print("Surface looks like")
    for row in network._surface._surface:
        print(row)

    frame = Frame(source_id='device1', dest_id='device2')
    network.transmit(frame, 900)


if __name__ == '__main__':
    surface = [
        [2, 2, 2, 1, 0, 1],
        [2, 0, 0, 0, 0, 2],
        [2, 0, 2, 0, 0, 2],
        [2, 0, 2, 2, 0, 2],
        [2, 0, 0, 0, 0, 2],
        [2, 1, 2, 2, 2, 2]
    ]
    run(surface)
