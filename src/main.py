import random

from DataInput import *
from src.client import *


def assignAgentSrcNodes() -> None:
    if numOfAgents == len(pokLst):
        for i in range(numOfAgents):
            client.add_agent("{\"id\":" + str(pokLst[i].node_src) + "}")
    elif numOfAgents < len(pokLst):
        for i in range(numOfAgents):
            client.add_agent("{\"id\":" + str(pokLst[i].node_src) + "}")
    else:  # numOfAgents > len(pokLst)
        for i in range(len(pokLst)):
            client.add_agent("{\"id\":" + str(pokLst[i].node_src) + "}")
        for i in range(numOfAgents - len(pokLst)):
            random.seed(a=0)
            rand = random.randint(len(graph))
            while rand not in graph.nodes:
                rand = random.randint(len(graph))
            client.add_agent("{\"id\":" + str(rand) + "}")



if __name__ == '__main__':
    # default port
    PORT = 6666
    # server host (default localhost 127.0.0.1)
    HOST = '127.0.0.1'
    client = Client()  # init of Client
    client.start_connection(HOST, PORT)  # init connection to server
    graph = loadGraph(client.get_graph())  # load the graph (as instance of networkx graph)
    pokLst = loadAllPokemons(client.get_pokemons(), graph)  # load Pokemon list
    caseInfo = json.loads(client.get_info())
    numOfAgents = caseInfo['GameServer']['agents']
    assignAgentSrcNodes()
    client.start()
    agentLst = loadAllAgents(client.get_agents())
    print(agentLst)
