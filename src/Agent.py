import json


class Agent:

    def __init__(self, id, value, src, dest, speed, pos):
        self.id = id
        self.value = value  # how many did the agent eat till now
        self.dest = dest
        self.src = src
        self.speed = speed
        self.pos = pos
        self.path = []
        self.all_agent = []

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

    def is_moving(self):  # TODO
        """If the agent is moving on edges"""

    def get_current_edge(self):  # TODO
        """retur the edge that the agent is currently on"""

    def loadAgent(self, file_name) -> bool:
        try:
            with open(file_name) as f:
                data = f.read()
            agent = json.loads(data)
            for i in agent['Agents']:
                self.all_agent.append(Agent(i['id'], i['value'],i['src'],i['dest'], i['speed'], i['pos']))
            # self.id = agent['id']
            # self.value = agent['value']
            # self.src = agent['src']
            # self.dest = agent['dest']
            # self.speed = agent['speed']
            # self.pos = agent['pos']

        except IOError as e:
            return False
        return True

    """

                "Agents":[
                    {
                        "Agent":
                        {
                            "id":0,
                            "value":0.0,
                            "src":0,
                            "dest":1,
                            "speed":1.0,
                            "pos":"35.18753053591606,32.10378225882353,0.0"
                        }
                    }
                ]

            """


