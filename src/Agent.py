class Agent:

    def __init__(self, id, value, src, dest, speed, pos):
        self.id = id
        self.value = value #how many did the agent eat till now
        self.dest = dest
        self.src = src
        self.speed = speed
        self.pos = pos
        self.path = {}

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

    def setPath(self, path):
        """Set the path the agent need to moove on to get the pokemon as fast as he can"""

        self.path = path

    def getPath(self):
        """Get the path the agent need to moove on to get the pokemon as fast as he can"""
        return self.path

    # def GetAgentsList(self):
    #     """Get a list of all the Agents"""

    def is_moving(self):
        """If the agent is moving on edges"""

    def get_current_edge(self):
        """retur the edge that the agent is currently on"""
