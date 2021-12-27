import json

from src.Node import Node
from src.GraphAlgo import *

class Graph:
    def __init__(self):
        self.Edges = {}
        self.Nodes = {}
        self.edge_size = 0

    def __str__(self):
        return "Graph: |V|=" + str(self.numOfNodes()) + " , |E|=" + str(self.numOfEdges())

    def numOfNodes(self) -> int:
        """return the number of nodes are in the graph"""
        return len(self.Nodes)

    def numOfEdges(self) -> int:
        return self.edge_size

    def getNode(self, key):
        """get node by id"""
        return self.Nodes.get(key)

    def getAllNodes(self) -> dict:
        """get all vertices in graph"""
        return self.Nodes

    def getEdgeWeight(self, src: int, dest: int):
        """get edge and return it weight"""
        return self.Edges[src][dest]

    def incomingEdgesToNode(self, id1: int):
        in_edges = {}
        for curr_src_key in self.Edges.keys():  # for each src key in the dictionary
            if id1 in self.Edges[curr_src_key]:  # if id1 is a valid destination node
                in_edges.update({curr_src_key: self.Edges[curr_src_key][id1]})  # {src: {dest: weight}}
        return in_edges

    def all_out_edges_of_node(self, id1: int):
        """get id of node and return dictionary of all edges OUT from it{src:{dest:weight}}"""
        try:
            return self.Edges[id1]
        except Exception:
            return None

    def addEdge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 not in self.Nodes or id2 not in self.Nodes:  # if one of the nodes or both don't exist
            return False
        if id1 in self.Edges and id2 in self.Edges[id1]:  # if edge exists (no matter its weight)
            return False
        if id1 in self.Edges:  # source node dict exists
            self.Edges.get(id1).update({id2: weight})
        else:  # source node dict doesn't exists
            self.Edges.update({id1: {id2: weight}})  # add new edge to the edge dictionary
        self.edge_size += 1  # add edge to the graph
        return True

    def addNode(self, node_id: int, pos=None) -> bool:
        if node_id in self.Nodes:  # if node already exist, we will not add it
            return False
        temp = Node(pos, node_id)
        self.Nodes.update({node_id: temp})  # add new node to the edge dictionary
        return True

    def removeNode(self, node_id: int) -> bool:
        if node_id not in self.Nodes:
            return False

        if node_id in self.Edges.keys():
            self.edge_size -= len(self.all_out_edges_of_node(node_id))  # decrease the number of edges in graph by 1
            self.Edges.pop(node_id)  # remove edges FROM node_id
        for curr_src in self.incomingEdgesToNode(node_id).keys():
            self.removeEdge(curr_src, node_id)  # remove edges TO
        self.Nodes.pop(node_id)  # remove node
        return True

    def removeEdge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 not in self.Edges and node_id2 not in self.Edges[node_id1]:  # edge doesnt exist
            return False
        if len(self.Edges[node_id1]) == 1:  # only destination from current src node
            self.Edges.pop(node_id1)  # remove the src node itself
        else:
            self.Edges[node_id1].pop(node_id2)
        self.edge_size -= 1  # decrease the number of edges in graph by 1
        return True

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
