from unittest import TestCase
from src.Pokemon import Pokemon
from src.DataInput import *


class test_DataInput(TestCase):

    def test_load_all_pokemons(self):
        s = '{"Pokemons":[{"Pokemon":{"value":5.0,"type":-1,"pos":"35.197656770719604,32.10191878639921,0.0"}}]}'
        graph = nx.DiGraph()
        p = loadAllPokemons(s, graph)
        self.assertEqual(p[0].value, 5.0)
        self.assertEqual(p[0].type, -1)
        pos = Point(x=35.197656770719604, y=32.10191878639921, z=0.0)
        self.assertEqual(p[0].pos.getX(), pos.getX())
        self.assertEqual(p[0].pos.getY(), pos.getY())

    def test_load_All_Agents(self):
        s1 = '{"Agents":[{"Agent":{"id":0,"value":0.0,"src":0,"dest":1,"speed":1.0,"pos":"35.18753053591606,32.10378225882353,0.0"}}]}'
        a = loadAllAgents(s1)
        self.assertEqual(a[0].id, 0)
        self.assertEqual(a[0].value, 0.0)
        self.assertEqual(a[0].src, 0)
        self.assertEqual(a[0].dest, 1)
        self.assertEqual(a[0].speed, 1.0)
        pos = Point(x=35.18753053591606, y=32.10378225882353, z=0.0)
        x= a[0].getPos().getX()
        self.assertEqual(a[0].getPos().getX(), pos.getX())
        self.assertEqual(a[0].getPos().getY(), pos.getY())

    def test_load_Graph(self):
        s2 = '{"Edges":[{"src":0,"w":1.4004465106761335,"dest":1},' \
            '{"src":0,"w":1.4620268165085584,"dest":10}],"Nodes":[{"pos":"35.18753053591606,32.10378225882353,0.0","id":0},{"pos":"35.18958953510896,32.10785303529412,0.0","id":1},' \
            '{"pos":"35.19341035835351,32.10610841680672,0.0","id":10}]}'
        g = loadGraph(s2)
        self.assertEqual(g.number_of_nodes(), 3)
        self.assertEqual(g.number_of_edges(), 2)








