import heapq
import json
import os
import sys
from typing import List

from src.Graph import Graph


def load_from_json(graph: Graph, file_name: str) -> bool:
    try:
        if file_name[0] == '.':
            file_name = file_name[1:]
        if file_name[0] == '.':
            file_name = file_name[1:]
        graph = Graph()
        root_dir = os.path.dirname(os.path.abspath(__file__))[:-4]
        if "Ex3_OOP" not in file_name:
            file_name = root_dir + '/' + file_name
        with open(file_name) as f:
            data = f.read()
            graph_algo = json.loads(data)
            for node in graph_algo["Nodes"]:
                try:
                    graph.addNode(node["id"], node["pos"])
                except Exception:
                    graph.addEdge(node["id"])

            for edge in graph_algo["Edges"]:
                graph.addEdge(edge["src"], edge["dest"], edge["w"])

    except IOError as e:
        return False
    return True


def dijkstra(graph: Graph, start):
    """Taken and adapted from: https://www.bogotobogo.com/python/python_Dijkstras_Shortest_Path_Algorithm.php"""
    for node in graph.getAllNodes().values():
        node.distance = sys.maxsize  # set distance to infinity for all nodes
        node.adjacent = {}  # {neighbor:weight}
        node.visited = False  # Mark all nodes as unvisited
        node.previous = None

    final_dijkstra = {}  # define new dict
    final_dijkstra.update({start.get_id(): [0, 0.5]})

    # Set the distance for the start node to zero
    start.set_distance(0)

    # Put tuple pair into the priority queue
    unvisited_queue = [(node.get_distance(), node) for node in graph.getAllNodes().values()]
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue) != 0:
        uv = heapq.heappop(unvisited_queue)  # Pops a vertex with the smallest distance
        current = uv[1]
        # we will change the edge as visited (means True)
        current.set_visited()  # turn to true

        # now I would like to create one long dictionary of all neighbors of current node
        All_neighbors = graph.outgoingEdgesFromNode(current.id)
        if All_neighbors is not None:
            for next_node_id in All_neighbors.keys():  # for next in All_neighbors:
                next_node = graph.getNode(next_node_id)
                if next_node.get_visited():  # if visited, skip
                    continue
                new_dist = current.get_distance() + All_neighbors[next_node_id]  # {dest_node_id: edge_weight}
                if new_dist < next_node.get_distance():
                    next_node.set_distance(new_dist)
                    next_node.set_previous(current)
                    # update the relevant value in the answer means:{node_id: [distance, previous_node_id]}
                    final_dijkstra.update({next_node.get_id(): [next_node.get_distance(), next_node.get_previous(
                        current).get_id()]})

        # Rebuild heap
        while len(unvisited_queue):  # Pop every item
            heapq.heappop(unvisited_queue)
        # Put all vertices not visited into the queue
        unvisited_queue = [(v.get_distance(), v) for v in graph.getAllNodes().values() if not v.visited]

        heapq.heapify(unvisited_queue)

        return final_dijkstra


def shortestPath(graph: Graph, id1: int, id2: int) -> (float, list):
    try:
        ans = []
        if graph is None or graph.getNode(id1) is None or graph.getNode(
                id2) is None:  # check if there is no path
            return float('inf'), []  # as requested
        if id1 == id2:
            return 0, [id1]  # if we get the sae node

        # dijkstra function return a dictionary with updated shortest path
        update_graph_dict = dijkstra(graph, graph.getNode(id1))
        if update_graph_dict[id2][0] == sys.maxsize:
            return float('inf'), []  # as requested

        curr_node_key = id2
        while curr_node_key != id1:  # go all over the dijkstra_dic
            ans.insert(0, curr_node_key)
            if update_graph_dict[curr_node_key][1] != 0.5:  # as we define before in dijkstra (the first element)
                curr_node_key = update_graph_dict[curr_node_key][1]
            else:
                break
        ans.insert(0, id1)  # add to the list all the nodes that append after id2
        return update_graph_dict[id2][0], ans
    except Exception:
        return float('inf'), []


def center(graph: Graph) -> (int, float):
    try:
        minMaxKey = sys.maxsize
        minMaxValue = sys.maxsize

        for currNode in graph.getAllNodes().values():  # we will move over all nodes in the graph
            # note that we get from dijkstra : {node_id: [distance, previous_node_id]}
            dijk_route = dijkstra(graph, currNode)
            currMaxVal = 0

            for value in dijk_route.values():  # for each value in the dictionary
                currVal = value[0]  # we will take the distance as currVal
                if currMaxVal < currVal:
                    currMaxVal = currVal
            if minMaxValue > currMaxVal:
                minMaxKey = currNode.get_id()
                minMaxValue = currMaxVal

        if minMaxValue == sys.maxsize:  # could be for example in case of empty graph
            return None

        return minMaxKey, minMaxValue

    except Exception:
        return None


def TSP(graph: Graph, node_lst: List[int]) -> (List[int], float):
    ret = []  # node list to be returned
    weight = 0
    if len(node_lst) == 0:  # check if the node's list is empty
        return None
    currNode = node_lst[0]
    ret.append(currNode)
    visitedNodes = []
    while len(node_lst) != 0:  # while there are still unvisited cities
        visitedNodes.append(currNode)  # add the current node to visitedNode list
        min_distance = sys.maxsize
        nextNode = currNode
        if currNode in node_lst:  # if currnode is in the node_lst we will remoove it
            node_lst.remove(currNode)
        path = []  # init ans list of nodes

        for node in node_lst:  # go all over the unvisited nodes, calculate the closest one
            if node not in visitedNodes:
                # print(self.shortest_path(currNode, node)[1])
                short_path_result = shortest_path(graph, currNode, node)
                curr_distance = short_path_result[0]
                if curr_distance < min_distance:
                    min_distance = curr_distance
                    nextNode = node
                    path = short_path_result[1]  # add the closest node to path list

        currNode = nextNode
        for node in path:  # The closest node's path (out of all cities) is appended to the list which is to be returned
            if node != path[0]:  # add all vertices if they are not the first item in the 'path' list
                ret.append(node)
                visitedNodes.append(node)  # add node to visitednodes list
                if node in node_lst:
                    node_lst.remove(node)
    if len(ret) == 0:
        return None
    for index in range(1, len(ret)):
        weight += graph.getEdgeWeight(ret[index-1], ret[index])

    return ret, weight
