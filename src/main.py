import time

from DataInput import *
from src.Algorithms import *

EPS = 0.000001

if __name__ == '__main__':
    # default port
    PORT = 6666
    # server host (default localhost 127.0.0.1)
    HOST = '127.0.0.1'
    client = Client()  # init of Client
    client.start_connection(HOST, PORT)  # init connection to server
    graph = loadGraph(client.get_graph())  # load the graph (as instance of networkx graph)
    pokLst = loadAllPokemons(client.get_pokemons(), graph)  # load Pokemon list
    caseInfo = json.loads(client.get_info())
    numOfAgents = caseInfo['GameServer']['agents']
    numOfAssignedAgents = assignAgentSrcNodes(numOfAgents, client, pokLst, graph)

    client.start()
    startTime = time.time()
    timeStamps = []
    agentLst = loadAllAgents(client.get_agents())
    for i in range(numOfAssignedAgents):  # choosing the next destination for nodes with assigned pokemons, adding
        # their destination to the agent's path
        client.choose_next_edge(
            '{"agent_id":' + str(agentLst[i].getId()) + ', "next_node_id":' + str(pokLst[i].getNodeDest()) + '}')
        agentLst[i].addToPath(pokLst[i].getNodeDest(), timeStamps)
        agentLst[i].addPokemonsListPerAgent(pokLst[i])
    client.move()

    while client.is_running() == 'true':
        if time.time() - timeStamps[0] < EPS:
            timeStamps.pop(0)
            client.move()
            agentLst = loadAllAgents(client.get_agents())

        for agent in agentLst:
            if agent.getDest() == -1:
                poppedNode = agent.removePathHead()
                client.choose_next_edge(
                    '{"agent_id":' + str(agent.getId()) + ', "next_node_id":' + str(agent.getPathHead()) + '}')
                if poppedNode == agent.getPokLstHead().get_node_src() and agent.getPathHead() == \
                        agent.getPokLstHead().get_node_dest():  # A new pokemon exists
                    pokLst =
