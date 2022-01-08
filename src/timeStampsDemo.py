import networkx as nx

from src.Agent import Agent


def initialTimeStamps(timestamps: list, graph: nx.DiGraph, agent: Agent, toAdd: float = 0) -> list:
    pokSrc = agent.getPokLst()[0].get_node_src()
    pokDest = agent.getPokLst()[0].get_node_dest()
    wholeEdgeLength = graph.nodes[pokSrc]['pos'].distance(graph.nodes[pokDest]['pos'])
    srcToPokLength = graph.nodes[agent.getPokLst()[0].get_node_src()]['pos'].distance(agent.getPokLst()[0].getPos())
    percentageOfEdge = srcToPokLength / wholeEdgeLength
    timeSrcToPok = percentageOfEdge * (graph.get_edge_data(pokSrc, pokDest)['weight'] / agent.get_speed())
    timestamps.append((toAdd + timeSrcToPok, agent.getId()))
    sorted(timestamps, key=lambda x: x[0])
    return timestamps


def pokemonTimeStamps(timestamps: list, graph: nx.DiGraph, agent: Agent, idPokDestNode: int) -> list:
    """function add the timeStamps when the agent visit the closest pokemon.
    Right now, we are at a POKEMON (at the middle of an edge)"""
    agentPath = agent.getPath()[:idPokDestNode]
    wholeEdgeLength = graph.nodes[agentPath[0]]['pos'].distance(graph.nodes[agentPath[1]]['pos'])
    currToDestLength = agent.getPos().distance(graph.nodes[agentPath[1]]['pos'])
    percentageOfEdge = currToDestLength / wholeEdgeLength
    timePokToDest = percentageOfEdge * (graph.get_edge_data(agentPath[0], agentPath[1])['weight'] / agent.get_speed())
    timestamps.append((timePokToDest, agent.getId()))
    # Got to path[1]. Need to get to next nodes + pokemon

    for nodeId in range(1, len(agentPath) - 2):
        currEdgeWeight = graph.get_edge_data(agentPath[nodeId], agentPath[nodeId + 1])['weight']
        timeToNextNode = currEdgeWeight / agent.speed
        timestamps.append((timestamps[-1][0] + timeToNextNode, agent.getId()))

    timestamps = initialTimeStamps(timestamps, graph, agent, toAdd=timestamps[-1][0])
    return timestamps
