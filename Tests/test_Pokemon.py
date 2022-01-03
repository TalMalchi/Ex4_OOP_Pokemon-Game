from unittest import TestCase
from src.Pokemon import Pokemon
import networkx as nx
from src.Point import Point


class test_Pokemon(TestCase):

    def test_find_src_dest(self):

        graph = nx.DiGraph()
        graph.add_node(1)
        graph.add_node(2)
        graph.add_node(3)
        graph.add_edge(1, 2)
        graph.add_edge(2, 3)
        graph.add_edge(1, 3)
        p= Pokemon(graph, 0, 1, Point(1 , 2, 0))
        #def __init__(self, graph: nx.DiGraph, value=0, type: int = 0, pos: Point = Point(), jsonStr=None):
        p.findSrcDest()
        self.assertEqual(p.get_node_src(), )

    def test_get_set_value(self):
        graph1 = nx.DiGraph()
        p = Pokemon(graph1, 0, 1, Point(1, 2, 0))
        self.assertEqual(p.getValue(), 0)
        p.setValue(4)
        self.assertEqual(p.getValue(), 4)
        p1 = Pokemon(graph1, 4, 1, Point(1, 2, 0))
        p.setValue(1)
        self.assertEqual(p.getValue(), 1)

    def test_get_set_type(self):
        graph1 = nx.DiGraph()
        p = Pokemon(graph1, 0, 1, Point(1, 2, 0))
        self.assertEqual(p.getType(), 1)
        p.setType(-1)
        self.assertEqual(p.getType(), -1)


    def test_get_set_pos(self):
        graph1 = nx.DiGraph()
        p = Pokemon(graph1, 0, 1, Point(1, 2, 0))
        self.assertEqual(p.pos.getX(), 1)
        self.assertEqual(p.pos.getZ(), 0)
        p.setPos(1, 4, 5)
        self.assertEqual(p.pos.getZ(), 5)



    def test_get_pos_string():
        assert False

    def test_get_node_dest():
        assert False

    def test_get_node_src():
        assert False

    def test_get_node_src():
        assert False

    def test_get_node_dest():
        assert False
