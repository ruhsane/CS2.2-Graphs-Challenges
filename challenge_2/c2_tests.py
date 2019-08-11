import unittest

from challenge2 import Graph
from challenge2 import Vertex

class VertexTest(unittest.TestCase):
    def test_bfs(self):
        graph = Graph()
        vertices = [
            Vertex(1), 
            Vertex(2),  
            Vertex(3),  
            Vertex(4),  
            Vertex(5)
        ]
        edges = [
            (1,2),
            (1,4),
            (2,3),
            (2,4),
            (2,5),
            (3,5)
        ]

        for vertex in vertices:
            graph.add_vertex(vertex)

        for edge in edges:
            from_vert, to_vert = edge
            graph.add_edge(from_vert, to_vert)


        test_path = graph.breadth_first_search(1, 5)
        test_edge = len(test_path) - 1
        actual_path = [1, 2, 5]
        actual_edges = 2
        self.assertEqual((test_path, test_edge), (actual_path, actual_edges))