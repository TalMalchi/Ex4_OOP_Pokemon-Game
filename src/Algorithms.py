import random

import networkx as nx

from src.client import Client


def assignAgentSrcNodes(numOfAgents: int, client: Client, pokLst: list, graph: nx.DiGraph) -> int:
    """Function to assign the agents their initial positions. returns the number of agents which have a pokemon to
    currently go to (if there are more agents than pokemons, not all agents might have a destination"""

    if numOfAgents == len(pokLst):
        # if the amount of agents is equals to the pokemon amount, we will put each agent next to each pokemon
        for i in range(numOfAgents):
            client.add_agent("{\"id\":" + str(pokLst[i].node_src) + "}")
            return numOfAgents
    elif numOfAgents < len(pokLst):  # else, we will put the agent next to the pokemon with the highest value
        for i in range(numOfAgents):
            client.add_agent("{\"id\":" + str(pokLst[i].node_src) + "}")
        return numOfAgents
    else:  # numOfAgents > len(pokLst) - else, we will set random position to each agent
        for i in range(len(pokLst)):
            client.add_agent("{\"id\":" + str(pokLst[i].node_src) + "}")
        for i in range(numOfAgents - len(pokLst)):
            random.seed(a=0)
            rand = random.randint(len(graph))
            while rand not in graph.nodes:
                rand = random.randint(len(graph))
            client.add_agent("{\"id\":" + str(rand) + "}")
        return len(pokLst)


