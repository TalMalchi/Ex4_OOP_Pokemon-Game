class Pokemon:

    def __init__(self, value, type, pos):
        self.value = value  # double value
        self.type = type  # -1 or 1
        self.pos = pos  # Location Class

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
