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
        return self.type

    def setType(self, type):
        self.type = type

    def getPos(self):
        return self.pos

    def setPos(self, pos):
        self.pos = pos
