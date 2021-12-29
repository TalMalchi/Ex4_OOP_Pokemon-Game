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
    agents = json.loads(client.get_agents(),
                        object_hook=lambda d: SimpleNamespace(**d)).Agents
    string = client.get_agents()
    agentLst = loadAllAgents(client.get_agents())
    graph_json = client.get_graph()
    print()