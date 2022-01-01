import networkx as nx

from src.Point import Point

EPS = 0.000001


class Pokemon:

    def __init__(self, graph: nx.DiGraph, value=0, type: int = 0, pos: Point = Point(), jsonStr=None):
        if jsonStr is not None:
            self.parsePokemon(jsonStr)
        else:
            self.value = value  # double value
            self.type = type  # -1 or 1
            self.pos = pos  # Location Class
        self.node_src = None
        self.node_dest = None
        self.findSrcDest(graph)

    def parsePokemon(self, jsonObj):
        """Function receives json object of pokemon and parses it, assigning values to current pokemon"""
        self.value = float(jsonObj['Pokemon']['value'])
        self.type = int(jsonObj['Pokemon']['type'])
        self.pos = Point(string=jsonObj['Pokemon']['pos'])

    def findSrcDest(self, graph: nx.DiGraph):
        for src, dest, weight in graph.edges(data="weight"):
            distSrcSelf = graph.nodes[src]['pos'].distance(self.pos)
            distSelfDest = graph.nodes[dest]['pos'].distance(self.pos)
            distEdge = graph.nodes[src]['pos'].distance(graph.nodes[dest]['pos'])
            if abs(distSrcSelf + distSelfDest - distEdge) < EPS:
                if dest > src and self.type > 0:
                    self.node_src = src
                    self.node_dest = dest
                    break
                elif dest < src and self.type < 0:
                    self.node_src = src
                    self.node_dest = dest
                    break

    def __str__(self):
        return "value: " + str(self.value) + ", type: " + str(self.type) + ", pos: " + str(self.pos) + "edge: (" + str(
            self.node_src) + ", " + str(self.node_dest) + ")"

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

    def getType(self):
        """get the direction of the edge (-1 or1)"""
        return self.type

    def setType(self, type):
        self.type = type

    def getPos(self):
        return self.pos

    def setPos(self, pos):
        self.pos = pos
