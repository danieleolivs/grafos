# Use este comando no terminal para executar esta suite de testes
# python -m unittest -v test/test_Q02.py
import unittest
import networkx as nx
from parameterized import parameterized
from src.Q02 import reachable

# Test Data
D1 = nx.DiGraph([(0, 1),(1, 2),(2, 8), (6, 8), (8, 2), (2, 6)])
D2 = nx.DiGraph([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)])
D3 = nx.DiGraph([(0,1), (1,3), (2,0), (3,1), (4,2)])

class Test_reachable (unittest.TestCase):

  @parameterized.expand([
      ['D1', D1, 0, []],
      ['D1', D1, 0, []],
      ['D1', D1, 8, [1, 0]],
      ['D2', D2, 0, [4, 3, 2, 1]],
      ['D2', D2, 2, [0, 5, 4, 3]],
      ['D2', D2, 1, [5, 4, 3, 2]],
      ['D3', D3, 0, [4]],
      ['D3', D3, 1, [2, 4]],
      ['D3', D3, 3, [0, 4, 2]]
  ])


  def test_base (self,name,G,x,expected_result):
    result = reachable(G,x)
    self.assertCountEqual(result, expected_result)

  def test_None (self):
    self.assertTrue(reachable(None,0) is None)  
    self.assertTrue(reachable(nx.DiGraph([(0,1)]),None) is None)   
  
  def test_Not_Digraph (self):
    self.assertTrue(reachable(nx.Graph([(0,1)]),0) is None)

  def test_Not_Vertex (self):
    self.assertTrue(reachable(nx.DiGraph([(0,1)]),4) is None) 

if __name__ == '__main__':
    unittest.main(verbosity=2)