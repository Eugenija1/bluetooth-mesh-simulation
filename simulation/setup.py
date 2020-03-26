from simulation.network import Network, Frame


def run(surface):
    network = Network(surface)
    print("Surface looks like")
    for row in network._radio_channels['1000'].surface:
        print(row)

    frame = Frame(source_id=1, dest_id=1)
    network.transmit(frame)


if __name__ == '__main__':
    surface = [
        [2, 2, 2, 1, 0, 1],
        [2, 0, 0, 0, 0, 2],
        [2, 1, 2, 2, 2, 2]
    ]
    run(surface)
