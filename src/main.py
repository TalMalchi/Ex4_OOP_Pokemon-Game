from DataInput import *
from src.Algorithms import *

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
    agentLst = loadAllAgents(client.get_agents())
    for i in range(numOfAssignedAgents):  # choosing the next destination for nodes with assigned pokemons, adding
        # their destination to the agent's path
        client.choose_next_edge(
            '{"agent_id":' + str(agentLst[i].getId()) + ', "next_node_id":' + str(pokLst[i].getNodeDest()) + '}')
        agentLst[i].addToPath(pokLst[i].getNodeDest())

