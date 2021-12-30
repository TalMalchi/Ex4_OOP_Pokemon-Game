import json
from types import SimpleNamespace

import networkx as nx
from src.Node import Node
from src.Point import Point
from src.client import *
from DataInput import *


if __name__ == '__main__':
    # graph = nx.DiGraph()
    # graph.add_node(Node(1, Point(0,2,4)))
    # node = graph.nodes.data()
    # print(graph)

    # default port
    PORT = 6666
    # server host (default localhost 127.0.0.1)
    HOST = '127.0.0.1'
    client = Client()
    client.start_connection(HOST, PORT)
    pokLst = loadAllPokemons(client.get_pokemons())
    graph = loadGraph(client.get_graph())

    client.add_agent("{\"id\":0}")
    client.start()
    agentLst = loadAllAgents(client.get_agents())
    print()
