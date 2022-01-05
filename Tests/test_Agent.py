from unittest import TestCase


class test_Agent(TestCase):

    pass


    def test_parse_agent(self):
        assert False

    def test_get_previous_node_time(self):
        assert False

    def test_set_previous_node_time(self):
        assert False

    def test_set_pos_vchange(self):
        assert False

    def test_get_pos_vchange(self):
        assert False

    def test_get_id(self):
        assert False
        # A = Agent(0, 1, 1, 2, 0.5, Point(1, 2, 0))

    #    def __init__(self, graph: nx.DiGraph, value=0, type: int = 0, pos: Point = Point(), jsonStr=None): pokemin

    # (self, id: int = 0, value: float = 0, src: int = 0, dest: int = 0, speed: float = 0,Point = Point(), jsonStr=None): #agent

    def test_get_value(self):
        assert False

    def test_set_value(self):
        assert False

    def test_get_speed(self):
        assert False

    def test_set_speed(self):
        assert False

    def test_get_pos(self):
        assert False

    def test_set_pos(self):
        assert False

    def test_get_src(self):
        assert False

    def test_set_src(self):
        assert False

    def test_get_dest(self):
        assert False

    def test_set_dest(self):
        assert False

    def test_add_to_path(self):
        assert False

    def test_get_path_head(self):
        assert False

    def test_remove_path_head(self):
        assert False

    def test_get_path(self):
        assert False

    def test_set_path(self):
        assert False

    def test_get_pok_lst(self):
        assert False

    def test_get_pok_lst_head(self):
        assert False

    def test_set_pok_lst(self):
        assert False

    def test_add_pokemons_list_per_agent(self):
        assert False

    def test_add_time_stamps(self):
        assert False

    def test_distance(self):
        assert False

    def test_find_curr_pos_of_agent(self):
        # (self, graph: nx.DiGraph)
        # test without changing speed
        graph = nx.DiGraph()
        graph.add_node(1, pos=Point(0, 0, 0))
        graph.add_node(2, pos=Point(1, 0, 0))
        graph.add_node(3, pos=Point(2, 0, 0))
        graph.add_edge(1, 2, weight=1)
        graph.add_edge(2, 3, weight=1)
        graph.add_edge(1, 3, weight=1)
        # (self, id: int = 0, value: float = 0, src: int = 0, dest: int = 0, speed: float = 0,Point = Point(), jsonStr=None): #agent

        a = Agent(0, 1, 1, 2, 1, Point(0, 0, 0))
        a.set_previous_node_time(time.time())
        a.set_pos_Vchange(Point(0, 0, 0))
        a.path = [1, 2, 3]
        time.sleep(0.5)

        ans = a.find_curr_pos_of_agent(graph)
        self.assertEqual(ans, (0.5, 0, 0))

        # # test with changing speed
        # A = Agent(0, 1, 1, 2, 0.5, Point(1, 2, 0))
        # A.set_speed(2)
        # # p = Pokemon(graph, 0, 1, Point(1, 2, 0))
