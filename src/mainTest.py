# from Pokemon import Pokemon
#
#
# def check0():
#     """
#     This function tests the naming (main methods of the DiGraph class, as defined in GraphInterface.
#     :return:
#     """
#     g = Graph()  # creates an empty directed graph
#     for n in range(4):
#         g.addNode(n)
#     g.addEdge(0, 1, 1)
#     g.addEdge(1, 0, 1.1)
#     g.addEdge(1, 2, 1.3)
#     g.addEdge(2, 3, 1.1)
#     g.addEdge(1, 3, 1.9)
#     g.removeEdge(1, 3)
#     g.addEdge(1, 3, 10)
#     print(g)  # prints the __repr__ (func output)
#     print(g.getAllNodes())  # prints a dict with all the graph's vertices.
#     print(g.incomingEdgesToNode(1))
#     print(g.outgoingEdgesFromNode(1))
#     print(shortestPath(g, 0, 3))
#
#
# # if __name__ == '__main__':
#
#
# # agent= Agent
# # agent.loadAgent("data/pagentTest.json")
