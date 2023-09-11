import networkx as nx
from gtufcg.util.networkx_util import draw_graph
from src.Q01 import non_neighbor

# Ambiente para testes manuais
G4 = nx.bull_graph()
print(f"Vértices: {G4.nodes}")
print(f"Arestas: {G4.edges}")
v = 0 
NS = non_neighbor(G4,v)
print(f"Não vizinhos de {v}: {NS}")
draw_graph(G4)