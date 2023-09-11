import networkx as nx
from gtufcg.util.networkx_util import draw_graph
from src.Q02 import reachable

D = nx.DiGraph([(0,1),(1,3),(2,0),(3,1),(4,2)])
print(reachable(D,0))
draw_graph(D)