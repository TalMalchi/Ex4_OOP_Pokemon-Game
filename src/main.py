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
        if time.time() - startTime - timeStamps[0] < EPS:
            timeStamps.pop(0)
            client.move()

        for i in range(len(agentLst)):
            if agentLst[i].getDest() == -1:  # agent arrived at intersection of nodes
                poppedNode = agentLst[i].removePathHead()  # node which was the src node of the agent's previous edge
                client.choose_next_edge(  # sending the agent towards the next node in its path
                    '{"agent_id":' + str(agentLst[i].getId()) + ', "next_node_id":' + str(
                        agentLst[i].getPathHead()) + '}')
                agentLst[i].set_previous_node_time(time.time())  # set time and place of change of speed
                agentLst[i].set_pos_Vchange(poppedNode)

            if agentLst[i].getPos().distance(agentLst[i].getPokLstHead().pos) < EPS:
                # A pokemon was eaten, a new pokemon exists on the graph
                pokLst = appendToAllPokemons(client.get_pokemons(), graph, pokLst)  # update pokemon list
                tempAgentLst = loadAllAgents(client.get_agents())  # temporarily load agents from client
                agentLst[i].speed = tempAgentLst[i].speed  # update current agents speed and pos
                agentLst[i].pos = tempAgentLst[i].pos

                agentLst[i].set_previous_node_time(time.time())  # set time and place of change of speed
                agentLst[i].set_pos_Vchange(agentLst[i].getPos())
                # TODO assign new pokemon
                # TODO fix timestamps. return from all functions or make dictionary and return from functions





                # if poppedNode == agent.getPokLstHead().get_node_src() and agent.getPathHead() == \
                #         agent.getPokLstHead().get_node_dest():  # A pokemon was eaten, a new pokemon exists on the graph
                #     pokLst =
