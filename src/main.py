import time

from DataInput import *
from src.Algorithms import *

EPS = 0.0001

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
    numOfAssignedAgentsToPok = assignAgentSrcNodes(numOfAgents, client, pokLst, graph)

    client.start()  # Game starts here (the timer, too)
    startTime = time.time()
    timeStamps = []  # list of tuples
    agentLst = loadAllAgents(client.get_agents())
    for i in range(numOfAssignedAgentsToPok):  # choosing the next destination for nodes with assigned pokemons, adding
        # their destination to the agent's path
        client.choose_next_edge(
            '{"agent_id":' + str(agentLst[i].getId()) + ', "next_node_id":' + str(pokLst[i].get_node_dest()) + '}')
        agentLst[i].addPokemonsListPerAgent(pokLst[i])
        timeStamps = agentLst[i].addToPath([pokLst[i].get_node_src(), pokLst[i].get_node_dest()], graph, timeStamps)
        # Update timestamps as well
    client.move()

    i = 0
    while client.is_running() == 'true':
        print(i)
        i+=1
        tempTime = time.time() - startTime
        if tempTime - timeStamps[0][0] < EPS:
            timeStamps.pop(0)
            client.move()
            print(client.get_info())
            for i in range(len(agentLst)):
                if agentLst[i].getDest() == -1:  # agent arrived at intersection of nodes
                    poppedNode = agentLst[i].removePathHead()  # node which was the src node of the agent's previous edge
                    client.choose_next_edge(  # sending the agent towards the next node in its path
                        '{"agent_id":' + str(agentLst[i].getId()) + ', "next_node_id":' + str(
                            agentLst[i].getPathHead()) + '}')
                    agentLst[i].set_previous_node_time(time.time())  # set time and place of change of speed
                    agentLst[i].setPassedPokPos(graph.nodes[poppedNode]['pos'])
                    if len(agentLst[i].getPath()) >= 2:
                        agentLst[i].setSrc(agentLst[i].getPath()[0])
                        agentLst[i].setDest(agentLst[i].getPath()[1])

                if agentLst[i].getPos().distance(agentLst[i].getPokLstHead().pos) < EPS:
                    # A pokemon was eaten, a new pokemon exists on the graph
                    pokLst = appendToAllPokemons(client.get_pokemons(), graph, pokLst)  # update pokemon list
                    tempAgentLst = loadAllAgents(client.get_agents())  # temporarily load agents from client
                    agentLst[i].speed = tempAgentLst[i].speed  # update current agents speed and pos
                    agentLst[i].pos = tempAgentLst[i].pos
                    agentLst[i].value = tempAgentLst[i].value
                    agentLst[i].set_previous_node_time(time.time())  # set time and place of change of speed
                    agentLst[i].setPassedPokPos(agentLst[i].getPos())

                    # assign new pokemon
                    agentLst, timeStamps = assignNewPokemonToAgent(graph, agentLst, pokLst[-1], timeStamps)

    print(client.get_info())







                # if poppedNode == agent.getPokLstHead().get_node_src() and agent.getPathHead() == \
                #         agent.getPokLstHead().get_node_dest():  # A pokemon was eaten, a new pokemon exists on the graph
                #     pokLst =
