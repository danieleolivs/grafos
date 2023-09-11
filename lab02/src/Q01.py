# Implemente a função **bipartite_complement** que recebe um grafo simples 
# bipartido **B1** como entrada, uma das partições de vértices **X** 
# (a partição Y é V(G)\X) e retorna um grafo bipartido **B2** onde:
#
#   * o conjunto de vértices de **B2** é o mesmo conjunto de vértices de **B1**
#   * as bipartições **X** e **Y** são as mesmas
#   * O conjunto de arestas de **B2** é formado por arestas (u,v) onde u pertence a X e v pertence a Y, mas (u,v)  não pertence a **B1**. 
#
# Como exemplo, considere o seguinte grafo bipartido:
#
#        V(B1) = {a,b,c,d}
#        E(B1) = {ac,bd,ad}
#        X = {a,b}
#
# O grafo B2 deve ser definido como:
#
#        V(B2) = {a,b,c,d}
#        E(B2) = {bc}
#
#**Dica**:
#* Use a função [create_empty_copy](https://networkx.org/documentation/stable/reference/generated/networkx.classes.function.create_empty_copy.html#create-empty-copy) 
# para criar um grafo com os mesmos vértices do grafo B1
import networkx as nx
from networkx.algorithms import bipartite

def bipartite_complement (B1,X):

  if B1 == None or X == None:
    return None

  if not nx.is_bipartite(B1):
      return None
  
  if not bipartite.is_bipartite_node_set(B1, X):
    return None

  for x in X:
    if not x in list(B1.nodes):
      return None

  B2 = nx.create_empty_copy(B1, with_data=True)
  Y = list(B2.nodes).copy()

  for x in X:
    if x in Y:
      Y.remove(x)
  
  for x in Y:
    for y in X:
      if not B1.has_edge(x, y):
        B2.add_edge(x, y)
    
  return B2


