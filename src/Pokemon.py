import math

from src.Point import Point


class Pokemon:

    def __init__(self, value=0, type: int = 0, pos: Point = Point(), jsonObj=None):
        if jsonObj is not None:
            self.loadPokemon(jsonObj)
        else:
            self.value = value  # double value
            self.type = type  # -1 or 1
            self.pos = pos  # Location Class
        self.node_src = None
        self.node_dest = None

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

    def find_dist_from_src(self):
        """find the distance from pokemon to node src """
        return math.dist(self.pos, self.node_src.pos)

    def find_dist_from_src(self):
        """find the distance from pokemon to node dest """
        return math.dist(self.pos, self.node_dest.pos)

    def loadPokemon(self, jsonObj):
        """Function receives json object of pokemon and parses it, assigning values to current pokemon"""
        self.value = jsonObj['Pokemon']['value']
        self.type = jsonObj['Pokemon']['type']
        Point(string=jsonObj['Pokemon']['pos'])
    # {
    #   "Pokemons": [
    #     {
    #       "Pokemon": {
    #         "value": 5.0,
    #         "type": -1,
    #         "pos": "35.197656770719604,32.10191878639921,0.0"
    #       }
    #     }
    #   ]
    # }
