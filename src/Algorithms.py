import random

import networkx as nx

from src.client import Client


def assignAgentSrcNodes(numOfAgents: int, client: Client, pokLst: list, graph: nx.DiGraph) -> None:
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
