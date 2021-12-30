import json

from src.Pokemon import Pokemon
from src.Agent import Agent
import networkx as nx
from src.Point import Point


def loadGraph(stringGraph):
    jsonGraph = json.loads(stringGraph)
    graph = nx.Graph()
    for node in jsonGraph["Nodes"]:
        graph.add_node(node["id"], pos=Point(string=node["pos"]))

    for edge in jsonGraph["Edges"]:
        graph.add_edge(edge["src"], edge["dest"], weight=edge["w"])

    return graph


def loadAllPokemons(pokemons):
    pokLst = []
    jsonTemp = json.loads(pokemons)
    for i in range(len(jsonTemp['Pokemons'])):
        pokLst.append(Pokemon(jsonStr=jsonTemp['Pokemons'][i]))
    return pokLst


def loadAllAgents(agents):
    agentLst = []
    jsonTemp = json.loads(agents)
    for i in range(len(jsonTemp['Agents'])):
        agentLst.append(Agent(jsonStr=jsonTemp['Agent'][i]))
    return agentLst
