import time

from DataInput import *
from src.Algorithms import *
from timeStampsDemo import *
from GUI.MainGUI import init


EPS = 0.01

if __name__ == '__main__':
    # default port
    PORT = 6666
    # server host (default localhost 127.0.0.1)
    HOST = '127.0.0.1'
    client = Client()  # init of Client
    client.start_connection(HOST, PORT)  # init connection to server
    graph = loadGraph(client.get_graph())  # load the graph (as instance of networkx graph)
    init(graph)

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
        client.choose_next_edge('{"agent_id":' + str(agentLst[i].getId()) + ', "next_node_id":' + str(pokLst[i].get_node_dest()) + '}')
        agentLst[i].addToPokList(pokLst[i])
        agentLst[i].addToPath([pokLst[i].get_node_src(), pokLst[i].get_node_dest()])  # add to list
    client.move()
    while client.is_running() == 'true':

        client.move()

        tempAgentLst = loadAllAgents(client.get_agents())  # temporarily load agents from client
        for i in range(len(agentLst)):
            agentLst[i].set_speed(tempAgentLst[i].speed)  # update current agents speed and pos
            agentLst[i].setPos(tempAgentLst[i].pos)
            agentLst[i].setValue(tempAgentLst[i].value)
            agentLst[i].setSrc(tempAgentLst[i].getSrc())
            agentLst[i].setDest(tempAgentLst[i].getDest())

            print(client.get_info())  # todo
            # print(agentLst[0])
            # print(agentLst[0].path)
            # print(agentLst[i].getSrc())
            # print(agentLst[i].getDest())
            # print(pokLst)
            # print()

            if agentLst[i].getDest() == -1:  # agent arrived at intersection of nodes
                poppedNode = agentLst[i].removePathHead()  # node which was the src node of the agent's previous edge
                stringToSend = '{"agent_id":' + str(agentLst[i].getId()) + ', "next_node_id":' + str(agentLst[i].getPath()[1]) + '}'
                client.choose_next_edge(stringToSend)  # sending the agent towards the next node in its path
                if len(agentLst[i].getPath()) >= 2:  # If the path of the agent is at least in length 2
                    agentLst[i].setSrc(agentLst[i].getPath()[0])  # Than the first element will be the source
                    agentLst[i].setDest(agentLst[i].getPath()[1])  # And the second element will be the destination

            if agentLst[i].getPos().distance(agentLst[i].getPokLstHead().pos) < 0.02:  # 0.02
                agentLst[i].popHeadPokLst()
                # A pokemon was eaten, a new pokemon exists on the graph
                pokLst = loadAllPokemons(client.get_pokemons(), graph)  # update pokemon list

                # print("totalPokList = " + str(loadAllPokemons(client.get_pokemons(), graph)))

                # assign new pokemon
                agentLst = assignNewPokemonToAgent(graph, agentLst, pokLst[-1])
            time.sleep(0.1)
    # print(client.get_info())  # todo
    # print(agentLst)
    # print(pokLst)
    # print()