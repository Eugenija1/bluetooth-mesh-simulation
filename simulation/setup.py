from simulation.network import Network, Frame


def run(surface):
    network = Network(surface)
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
