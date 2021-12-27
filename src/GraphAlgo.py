import json
import os

from src.Graph import Graph
from py4j.java_gateway import JavaGateway
gateway = JavaGateway()


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

