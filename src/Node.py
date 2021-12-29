import sys

from src.Point import Point


class Node:
    # static variables, for GUI
    min_value = Point(-sys.maxsize, -sys.maxsize, -sys.maxsize)
    max_value = Point(sys.maxsize, sys.maxsize, sys.maxsize)

    def __init__(self, id: int, pos=Point()):
        self.id = id
        if pos == 'None' or pos is None:  # if pos is None we will initialize all x,y,z values to none
            self.x = None
            self.y = None
            self.z = None
        else:
            self.x = pos.getX()
            self.y = pos.getY()
            self.z = pos.getZ()
            # define min max values to present the graph
            if Node.min_value.getX() < self.x:
                Node.min_value.setX(self.x)
            if Node.min_value.getY() < self.y:
                Node.min_value.setY(self.y)
            if Node.min_value.getZ() < self.z:
                Node.min_value.setZ(self.z)

            if Node.max_value.getX() > self.x:
                Node.max_value.setX(self.x)
            if Node.max_value.getY() > self.y:
                Node.max_value.setY(self.y)
            if Node.max_value.getZ() > self.z:
                Node.max_value.setZ(self.z)

        self.distance = sys.maxsize  # set distance to infinity for all nodes
        self.adjacent = {}  # {neighbor:weight}
        self.visited = False  # Mark all nodes as unvisited
        self.previous = None

    def __str__(self):
        """toString function"""
        return str("id: " + str(self.id))

    def __hash__(self):
        return hash(id(self))

    def getID(self) -> int:
        """get id of node"""
        return self.id

    def getPos(self) -> Point:
        return self.id

    def get_visited(self):
        """get visited to see the status of the visited attribute of the node"""
        return self.visited

    def get_distance(self):
        return self.distance

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_previous(self, prev):
        """node1.set_previous(cur) -> set cur as previous node of node1"""
        self.previous = prev

    def set_distance(self, dist):
        self.distance = dist

    def get_previous(self, current):
        """get previous node of given node"""
        return self.previous

    def set_visited(self):
        """initializes attribute as defoltive true boolean value"""
        self.visited = True

    # for using heapq.heapify in GraphAlgo-we will define comparators

    def __eq__(self, other):
        return self.id == other.id

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return self.id < other.get_id()

    def __gt__(self, other):
        return self.id > other.id

    def __le__(self, other):
        return (self < other) or (self == other)

    def __ge__(self, other):
        return (self > other) or (self == other)
