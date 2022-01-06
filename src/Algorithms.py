import random
import sys

import networkx as nx

from src.Pokemon import Pokemon
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


def tsp(graph: nx.DiGraph, nodesToVisit: list):
    """Calculates the shortest path between a list of nodes, given the graph. Does not calculate the time needed to
    traverse (it is also dependent on speed of agent."""
    shortestPathDist = sys.maxsize
    minj = 0
    totalDist = 0
    shortestPath = []
    for i in range(len(nodesToVisit)):
        for j in range(len(nodesToVisit)):
            currShortestPathDist = nx.shortest_path_length(graph, source=i, target=j)
            if shortestPathDist > currShortestPathDist:
                minj = j
                shortestPathDist = currShortestPathDist
        totalDist += shortestPathDist
        shortestPath.append(nx.shortest_path(graph, source=i, target=minj))
        nodesToVisit.pop(i)
    return totalDist, shortestPath


def assignNewPokemonToAgent(graph: nx.DiGraph, agentLst: list, pokemon: Pokemon, timeStamps: list):
    """Chooses the best agent to allocate the new pokemon to, using TSP. Returns the ID of the agent which was chosen
    for the new pokemon"""
    minDist = sys.maxsize
    minPath = []
    minLst = []
    minAgentId = 0
    for i in range(len(agentLst)):
        tempLst = agentLst[i].getPokLst().append(pokemon)
        tempShortDist, tempShortPath = tsp(graph, tempLst)
        if minDist > tempShortDist:
            minDist = tempShortDist
            minPath = tempShortPath
            minAgentId = i
            minLst = tempLst
    agentLst[minAgentId].setPokLst(minLst)
    timeStamps = agentLst[minAgentId].setPath(minPath, graph, timeStamps)
    return agentLst, timeStamps
