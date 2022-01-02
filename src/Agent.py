import networkx as nx

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
        self.path = []

    def parseAgent(self, jsonStr):
        """Function receives json object of pokemon and parses it, assigning values to current pokemon"""
        self.id = jsonStr['id']
        self.value = jsonStr['value']
        self.src = jsonStr['src']
        self.dest = jsonStr['dest']
        self.speed = jsonStr['speed']
        self.pos = Point(jsonStr['speed'])

    def __str__(self):
        return "{id: " + str(self.id) + ", value: " + str(self.value) + ", src: " + str(self.src) + ", dest: " + str(
            self.dest) + ", speed: " + str(self.speed) + ", pos: " + str(self.pos) + ", path: " + str(self.path)

    def __repr__(self):
        return self.__str__()

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
        self.addTimeStamps(graph, timeStamps, lst)

    def getPathHead(self):
        return self.path[0]

    def removePathHead(self):
        temp = self.path[0]
        self.path.pop(0)
        return temp

    def getPath(self):
        """Get the path the agent need to moove on to get the pokemon as fast as he can"""
        return self.path

    def getPokLst(self):
        """get the list of pokemons for each agent"""
        return self.Pokemons_forAgent

    def getPokLstHead(self) -> Pokemon:
        """get the list of pokemons for each agent"""
        return self.Pokemons_forAgent[0]

    def setPokemonsListPerAgent(self, PokemonsListPerAgent):
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
    #     """retur the edge that the agent is currently on"""

    def addTimeStamps(self, graph: nx.DiGraph, timeStamps: list, pathToAdd: list):  # total time to path an edge
        total_time = 0
        for i in range(len(pathToAdd)):  # go all over the agent's path
            for j in self.Pokemons_forAgent:
                if i is j.node_src and i + 1 is j.node_dest:
                    dist_src_dst = graph.nodes[j.node_src]['pos'].distance.graph.nodes[j.node_dest]['pos']
                    dist_pokemon_src = graph.nodes[j.node_src]['pos'].distance.graph.nodes[j.pos]
                    total_dist = dist_src_dst - dist_pokemon_src
                    total_time = total_dist(graph.get_edge_data(j.node_src, j.node_dest)['weight'] / self.speed)
                timeStamps.append(total_time)
        timeStamps.sort()

    def findLocation(self,graph: nx.DiGraph):
        for i in
            m = (dest_node_y - src_node_y) / (dest_node_x - src_node_x)  # m in the linear function y = mx + b
            b = dest_node_y - (m * dest_node_x)
