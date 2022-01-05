import math
import time

import networkx as nx
from sympy import Eq  # importing library sympy

from src.Point import Point
from src.Pokemon import Pokemon


class Agent:

    def __init__(self, id: int = 0, value: float = 0, src: int = 0, dest: int = 0, speed: float = 0,
                 pos: Point = Point(), jsonStr=None):
        self.PokemonsListPerAgent = None
        if jsonStr is not None:
            self.parseAgent(jsonStr)
        else:
            self.id = id
            self.value = value  # how many did the agent eat till now
            self.dest = dest
            self.src = src
            self.speed = speed
            self.pos = pos
            # Do Not add anything else to "else"
        self.Pokemons_forAgent = []
        self.Previous_node_time = 0  # this is the time that passed from the start of travel from previous node
        self.pos_Vchange = Point  # this is the position that the agent changed his speed
        self.path = []

    def parseAgent(self, jsonStr):
        """Function receives json object of pokemon and parses it, assigning values to current pokemon"""
        self.id = jsonStr['id']
        self.value = jsonStr['value']
        self.src = jsonStr['src']
        self.dest = jsonStr['dest']
        self.speed = jsonStr['speed']
        self.pos = Point(string=jsonStr['pos'])

    def __str__(self):
        return "{id: " + str(self.id) + ", value: " + str(self.value) + ", src: " + str(self.src) + ", dest: " + str(
            self.dest) + ", speed: " + str(self.speed) + ", pos: " + str(self.pos) + ", path: " + str(self.path)

    def __repr__(self):
        return self.__str__()

    def get_previous_node_time(self):
        """the time that passed from the start of travel from previous node"""
        return self.Previous_node_time

    def set_previous_node_time(self, Previous_node_time):
        """set the time that passed from the start of travel from previous node"""
        self.Previous_node_time = Previous_node_time

    def set_pos_Vchange(self, pos_Vchange: Point):
        """set the position that the agent changed his speed"""
        self.pos_Vchange = pos_Vchange

    def get_pos_Vchange(self) -> Point:
        """get the position that the agent changed his speed"""
        return self.pos_Vchange

    def getId(self):
        """get the id of the agent"""
        return self.id

    def getValue(self):
        """get the value of the agent"""
        return self.value

    def setValue(self, val):
        """set the value of the agent"""
        self.value = val

    def get_speed(self):
        """get the speed of the agent"""
        return self.speed

    def set_speed(self, sp):
        """set the speed of the agent"""
        self.speed = sp

    def getPos(self):
        return self.pos

    def setPos(self, pos):
        self.pos = pos

    def getSrc(self):
        return self.src

    def setSrc(self, src):
        self.src = src

    def getDest(self):
        return self.dest

    def setDest(self, dest):
        self.dest = dest

    def addToPath(self, lst: list, graph: nx.DiGraph, timeStamps: list):
        """Set the path the agent needs to move on to get the pokemon as fast as he can"""
        self.path.append(lst)
        return self.addTimeStamps(graph, timeStamps, lst)  # TODO edit

    def getPathHead(self):
        return self.path[0]

    def removePathHead(self):
        temp = self.path[0]
        self.path.pop(0)
        return temp

    def getPath(self):
        """Get the path the agent need to move on to get the pokemon as fast as he can"""
        return self.path

    def setPath(self, path: list, lstToAdd: list, graph: nx.DiGraph, timeStamps: list):
        self.path = path

    def getPokLst(self):
        """get the list of pokemons for each agent"""
        return self.Pokemons_forAgent

    def getPokLstHead(self) -> Pokemon:
        """get the list of pokemons for each agent"""
        return self.Pokemons_forAgent[0]

    def setPokLst(self, PokemonsListPerAgent):
        self.PokemonsListPerAgent = PokemonsListPerAgent

    def addPokemonsListPerAgent(self, pok):
        self.PokemonsListPerAgent.append(pok)

    def addTimeStamps(self, graph: nx.DiGraph, timeStamps: list, pathToAdd: list, startTime):
        """timestamps := list of the timestamps when the 'move' method from client should be called"""
        total_time = 0
        for i in range(len(pathToAdd) - 1):  # go all over the agent's path
            for j in self.Pokemons_forAgent:
                if i == j.node_src and (i + 1) == j.node_dest:
                    dist_src_dst = graph.nodes[j.node_src]['pos'].distance.graph.nodes[j.node_dest]['pos']
                    dist_pokemon_src = graph.nodes[j.node_src]['pos'].distance(graph.nodes[j.pos])
                    total_dist = dist_src_dst - dist_pokemon_src
                    total_time = total_dist(graph.get_edge_data(j.node_src, j.node_dest)['weight'] / self.speed)
                timeStamps.append(startTime + total_time)
        timeStamps.sort()
        return timeStamps

    def quadratic(self, a, b, c):
        """Method to calculate the results of a quadratic equation (2 values)"""
        x1 = ((-b) + math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
        x2 = ((-b) - math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
        return x1, x2

    def find_curr_pos_of_agent(self, graph: nx.DiGraph) -> Point:
        """function get agent and return his current position (Point)"""
        xStart = self.get_pos_Vchange().getX()
        yStart = self.get_pos_Vchange().getY()
        # TODO add if to handle y=c function
        xEnd = graph.nodes[self.getPath()[1]]['pos'].getX()
        yEnd = graph.nodes[self.getPath()[1]]['pos'].getY()

        weight = graph.get_edge_data(self.path[0], self.path[1])['weight']
        currTime = time.time() - self.Previous_node_time
        dist = self.speed * currTime  # S=VT

        m = (yStart - yEnd) / (xStart - xEnd)
        b = yStart - (m * xStart)  # y=Mx+b -> b=y-Mx

        qa = (m ** 2) + 1
        qb = (2 * b * m) - (2 * m * yStart) - (2 * xStart)
        qc = (b ** 2) - (2 * yStart * b) + (xStart ** 2) - (dist ** 2)

        x1, x2 = self.quadratic(qa, qb, qc)
        y1 = m*x1 + b
        y2 = m*x2 + b
        p1 = Point(x1, y1)
        p2 = Point(x2, y2)
        destP = graph.nodes[self.getPath()[1]]['pos']
        if self.get_pos_Vchange().distance(p1) + p1.distance(destP) == self.get_pos_Vchange().distance(destP):
            return p1
        else:
            return p2
