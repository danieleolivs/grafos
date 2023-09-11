import networkx as nx
from gtufcg.util.networkx_util import draw_graph
from src.Q01 import bipartite_complement

G1 = nx.path_graph(5)
print(f"V(G1): {G1.nodes}")
print(f"E(G1): {G1.edges}\n") 
X,Y = nx.bipartite.sets(G1)
print(f"X: {X}")
print(f"Y: {Y}\n")
G2 = bipartite_complement(G1,X)
print(f"V(G2): {G2.nodes}")
print(f"E(G2): {G2.edges}\n") 
# Desenhando o grafo com arestas de G1 e G2
draw_graph(nx.compose(G1,G2),nx.bipartite_layout(G1,X),
           eset=[G1.edges,G2.edges],esetcolor=["blue","pink"],
           esetlabel=["E(G1)", "E(G2)"])
