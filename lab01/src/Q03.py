# Escreva uma função, graph_types, que classifica um grafo não-direcionado, 
# considerando as seguintes categorias: 
#     Simples, Multigrafo, Pseudografo, Trivial, Nulo, Vazio, Bipartido. 
# Um mesmo grafo pode possuir mais de uma destas características. 
# Por exemplo, o grafo Trivial é também um grafo Simples, Vazio e Bipartido. 
# A função deve retornar uma lista com todas as classificações que podem ser 
# dadas ao grafo recebido como parâmetro, em qualquer ordem.
# Dicas:
#    Use o método number_of_edges da classe Graph para determinar a quantidade de arestas 
#    entre dois vértices (ver exercícios resolvidos Aula 02)
#    Use a função number_of_selfloops da seção Functions de NetworkX para determinar 
#    se o grafo possui loops
#    Use a função is_bipartite para testar se o grafo é bipartido

import networkx as nx

def graph_types (G):
  tipos = []

  if len(G.nodes) == 0:
    tipos.append('Nulo')

  if len(G.edges) == 0:
    tipos.append('Vazio')

  if nx.is_bipartite(G):
    tipos.append('Bipartido')

  if len(G.nodes) == 1 and len(G.edges) == 0:
    tipos.append('Trivial')

  for x in G.nodes:
    for y in G.nodes:
      if G.number_of_edges(x, y) > 1:
        tipos.append('Multigrafo')

  if nx.number_of_selfloops(G) > 0 and "Multigrafo" in tipos:
      tipos.append('Pseudografo')

  if nx.number_of_selfloops(G) > 0:
      tipos.append('Pseudografo')

  if not "Multigrafo" in tipos and not "Pseudografo" in tipos:
    tipos.append('Simples')

  return set(tipos)
