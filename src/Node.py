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

    def getID(self) -> int:
        """get id of node"""
        return self.id

    def getPos(self) -> Point:
        return self.id
