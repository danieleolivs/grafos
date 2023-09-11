# Use este comando no terminal para executar esta suite de testes
# python -m unittest -v test/test_Q01.py

import unittest
import networkx as nx
from parameterized import parameterized
from src.Q01 import bipartite_complement

# Test Data
Trivial = nx.complete_graph(1)
K2 = nx.complete_graph(2)
E2 = nx.empty_graph(2)
K3_3 = nx.complete_multipartite_graph([0,1,2],[3,4,5])
E6 = nx.empty_graph(6)
DC1 = nx.Graph([(0,1),(9,3),(8,4)])
DC2 = nx.Graph([(0, 3), (0, 4), (1, 9), (1, 8), (9, 4), (3, 8)])
K3 = nx.complete_graph(3)

class Test_bipartite_complement (unittest.TestCase):

  @parameterized.expand([
      ['Grafo Trivial', Trivial, [0], Trivial],
      ['K2',K2,[0],E2],
      ['K3_3',K3_3,[0,1,2],E6],
      ['E6',E6,[0,1,2],K3_3],
      ['DC1',DC1,[0,9,8],DC2]
  ])

  def test_base (self,name,G,X,expected_result):
    result = bipartite_complement(G,X)
    self.assertCountEqual(list(result.nodes),list(expected_result.nodes))
    self.assertEqual(result.number_of_edges(),expected_result.number_of_edges())
    self.assertTrue(all(result.has_edge(u,v) for u,v in expected_result.edges))

  def test_None (self):
    self.assertTrue(bipartite_complement(None,[0,1]) is None)  
  
  def test_None_set (self):
    self.assertTrue(bipartite_complement(K3_3,None) is None)

  def test_not_bipartite (self):
    self.assertTrue(bipartite_complement(K3,[0,1]) is None)

  def test_not_valid_set (self):
    self.assertTrue(bipartite_complement(K3_3,[9,10]) is None)

  def test_not_valid_partition (self):
    self.assertTrue(bipartite_complement(K3_3,[0,1]) is None)

if __name__ == '__main__':
    unittest.main(verbosity=2)