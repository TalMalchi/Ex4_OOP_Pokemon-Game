import json
from types import SimpleNamespace

import networkx as nx
from src.Node import Node
from src.Point import Point
from src.client import *
from DataInput import *


if __name__ == '__main__':
    # default port
    PORT = 6666
    # server host (default localhost 127.0.0.1)
    HOST = '127.0.0.1'
    client = Client()  # init of Client
    client.start_connection(HOST, PORT)  # init connection to server
    graph = loadGraph(client.get_graph())  # load the graph (as instance of networkx graph)
    pokLst = loadAllPokemons(client.get_pokemons(), graph)  # load Pokemon list

    client.add_agent("{\"id\":0}")
    client.start()
    agentLst = loadAllAgents(client.get_agents())
    print()
