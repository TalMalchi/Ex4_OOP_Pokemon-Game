import math

import networkx as nx
from sympy import symbols, Eq, solve  # importing library sympy

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
            self.Pokemons_forAgent = []
            self.Previous_node_time = 0  # this is the time that passed from the start of tavel from previous node
            self.pos_Vchange = (int, int)  # this is the position that the agent changed his speed
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

    def set_pos_Vchange(self, pos_Vchange):
        """set the position that the agent changed his speed"""
        self.pos_Vchange = pos_Vchange

    def get_pos_Vchange(self):
        """get the position that the agent changed his speed"""
        return self.pos_Vchange

    def getId(self):
        """get the id of the agent"""
        return self.id

    def getValue(self):
        """get the value of the agent"""
        return self.value

    def get_speed(self):
        """get the speed of the agent"""
        return self.speed

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
        return self.addTimeStamps(graph, timeStamps, lst)

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

    # def GetAgentsList(self):
    #     """Get a list of all the Agents"""
    #
    # def is_moving(self):  #
    #     """If the agent is moving on edges"""
    #
    # def get_current_edge(self):  #
    #     """return the edge that the agent is currently on"""

    def addTimeStamps(self, graph: nx.DiGraph, timeStamps: list, pathToAdd: list, startTime):
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

    def distance(point1, point2) -> float:
        """Calculate distance between the two points"""
        return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

    #    def find_curr_pos_of_agent(self, graph: nx.DiGraph) -> (int, int):
    #         """function get agent and return his current position (X,Y)"""
    #         # defining symbols used in equations
    #         # or unknown variables
    #         X_Agent, Y_Agent = symbols('X_Agent,Y_Agent')
    #         Xstart = graph.getnode(self.getPath[0]).getX()
    #         Ystart = graph.getnode(self.getpath[0]).getY()
    #
    #         Xend = graph.getnode(self.getPath[1]).getX()
    #         Yend = graph.getnode(self.getPath[1]).getY()
    #         # copmute M by: y=MX+B with those 2 points
    #         M = (Ystart - Yend) / (Xstart - Xend)
    #         # than compute below 2 different equation (with:https://www.geeksforgeeks.org/python-solve-the-linear-equation-of-multiple-variable/)  to find X_Agent,Y_Agent (we already know M)
    #         # defining equations
    #
    #         eq1 = Eq(((Ystart - Y_Agent) / (Xstart - X_Agent)), M)  # first equation
    #         eq2 = Eq(((Yend - Y_Agent) / (Xend - X_Agent)), M)  # sec equ
    #         # Creating an empty Dictionary
    #         AnsDict = {}
    #
    #         AnsDict = solve((eq1, eq2), (X_Agent, Y_Agent))
    #         return (AnsDict[X_Agent], AnsDict[Y_Agent])
    # # for i in
    # # m = (dest_node_y - src_node_y) / (dest_node_x - src_node_x)  # m in the linear function y = mx + b
    # # b = dest_node_y - (m * dest_node_x)

    def find_curr_pos_of_agent(self, graph: nx.DiGraph) -> (int, int):
        """function get agent and return his current position (X,Y)"""
        Pos_speed_change = self.get_pos_Vchange()
        Xstart = graph.nodes[self.getPath()[0]].getX()
        Ystart = graph.nodes[self.getPath()[0]].getY()

        Xend = graph.nodes[self.getPath()[1]].getX()
        Yend = graph.nodes[self.getPath()[1]].getY()
        # copmute M by: y=MX+B with those 2 points
        M = (Ystart - Yend) / (Xstart - Xend)
        # y=Mx+b -> b=y-Mx
        b = Ystart - (M * Xstart)

        # distanceTwoPoints=Pos_speed_change.distance(Xstart,Ystart)
        # X=VT->
        speedOfAgent = self.speed
        time = self.Previous_node_time
        dist = speedOfAgent * time
        # defining symbols used in equations
        # or unknown variables
        X_Agent, Y_Agent = symbols('X_Agent,Y_Agent')
        # defining equations
        eq1 = Eq(math.sqrt(((Xstart - X_Agent) ** 2) + (Ystart - Y_Agent) ** 2), M)  # first equation
        # y=Mx+b -> b=y-Mx
        eq2 = Eq((Y_Agent - M * X_Agent), b)  # sec
        # then computing below 2 different equations to find X_Agent,Y_Agent (we already know M)
        # adapted from: with:https://www.geeksforgeeks.org/python-solve-the-linear-equation-of-multiple-variable/

        AnsDict = solve((eq1, eq2), X_Agent, Y_Agent)
        return AnsDict[X_Agent], AnsDict[Y_Agent]
