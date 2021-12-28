class Point:
    def __init__(self, x=0, y=0, z=0, string: str = None):
        if string is not None:
            lst = string.split(',')
            self.x = lst[0]
            self.y = lst[1]
            self.z = lst[2]
        else:
            self.x = x
            self.y = y
            self.z = z

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getZ(self):
        return self.z

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def setZ(self, z):
        self.z = z
