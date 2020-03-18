"""Desribes classes used for `Node` communication."""
from simulation.physical_objects import Surface


class Network:
    """Describes medium where all communication happend."""

    def __init__(self, map: 'Some format of map'):
        self.radio_channels = {
            '1000': Surface(map),
            '1220': Surface(map)
        }

    def add_vertex(v):
      global graph
      global vertices_no
      if v in graph:
        print("Vertex ", v, " already exists.")
      else:
        vertices_no = vertices_no + 1
        graph[v] = []

    def add_edge(v1,v2):
      global graph
      if v1 not in graph:
        print("Vertex ", v1, " does not exist.")
      elif v2 not in graph:
        print("Vertex ", v2, " does not exist.")
      else:
        temp = [v2]
        graph[v1].append(temp)

    # Print the graph
    def print_graph(self):
      global graph
      for vertex in graph:
        for edges in graph[vertex]:
          print(vertex, " -> ", edges[0])



    def read_data(file):
        data = []
        with open(file,'r',encoding='utf-8')as f:
            for line in f :
                parts = line.split(",")
                for item in parts:
                    data.append(int(item))
        return data

    file = read_data('graph.txt')
    print(file)

    graph = {}


