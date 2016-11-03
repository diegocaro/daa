def adjacencymatrix(V, E):
  adj = [ [0 for _ in range(V) ] for _ in range(V) ]
  for u,w in E:
    adj[u][w] = 1
  return adj
  
def adjacencylist(V, E):
  adj = [ list() for _ in range(V) ]
  for u,w in E:
    adj[u].append(w)
  return adj


if __name__=='__main__':
  from pprint import pprint
  V = 13
  E = [ (0,1), (0,2), (0,6), (6,4), (4,3), (3,5), \
      (4,5), (7,8), (9,10), (9,11), (9,12), (11,12)]

  print("Matriz de adyacencia: ")
  pprint(adjacencymatrix(V, E))
  
  print("List de adyacencia: ")
  pprint(adjacencylist(V, E))