
# Escreva uma função, **non_neighbor**, que recebe um grafo *G* como entrada, 
# um identificador *v* de um vértice deste grafo e retorna uma lista com os 
# vértices que não são vizinhos de *v*. Se *v* não pertence ao grafo ou 
# *G* é nulo ou *None*, a função deve retornar *None*.

import networkx as nx;

def non_neighbor (G, v):

  if  G == None:
    return None

  if len(list(G.nodes)) == 0:
    return None

  if not v in list(G.nodes):
    return None

  nonNeighbor = list(nx.non_neighbors(G, v))
  edges = list(G.edges)

  if not (v, v) in edges:
    nonNeighbor.append(v)
  
  return sorted(nonNeighbor)

