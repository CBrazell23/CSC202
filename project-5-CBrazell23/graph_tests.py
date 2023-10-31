import unittest
from graph import *

class TestList(unittest.TestCase):

    def testAddV(self):
        g = Graph('test1.txt')
        g.add_vertex("v3")
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5'], ['v6', 'v7', 'v8', 'v9']])
        g.add_vertex("v12")
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5'], ["v12"], ['v6', 'v7', 'v8', 'v9']])

    def testGetVertex(self):
        g = Graph('test1.txt')
        self.assertEqual(g.get_vertex("v3").id, "v3")
        with self.assertRaises(AttributeError):
            g.get_vertex("Bananas").id

    def testGetVertices(self):
        g = Graph('test3.txt')
        self.assertEqual(g.get_vertices(), ["v1", "v2"])
        g = Graph('test2.txt')
        self.assertEqual(g.get_vertices(), ['v1', 'v1', 'v2', 'v2', 'v3', 'v3', 'v4', 'v4', 'v4', 'v6', 'v7', 'v8'])

    def testConn(self):
        g = Graph('test3.txt')
        self.assertEqual(g.conn_components(), [["v1", "v2"]])
        g = Graph('test2.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3'], ['v4', 'v6', 'v7', 'v8']])
        g = Graph('test1.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5'], ['v6', 'v7', 'v8', 'v9']])

    def testBi(self):
        g = Graph('test2.txt')
        self.assertFalse(g.is_bipartite())
        g = Graph('test1.txt')
        self.assertTrue(g.is_bipartite())

    def test_01(self):
        g = Graph('test1.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5'], ['v6', 'v7', 'v8', 'v9']])
        self.assertTrue(g.is_bipartite())
        
    def test_02(self):
        g = Graph('test2.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3'], ['v4', 'v6', 'v7', 'v8']])
        self.assertFalse(g.is_bipartite())

if __name__ == '__main__':
   unittest.main()
