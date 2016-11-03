from graph import adjacencylist
from collections import deque

import sys

def BreadthFirstSearch(G, s):
    marked = [False for _ in range(len(G))]
    edgeto = [None for _ in range(len(G))]
    distto = [sys.maxsize for _ in range(len(G))]
    
    bfs(G, s, marked, edgeto, distto)
    return marked, edgeto, distto

def bfs(G, u, marked, edgeto, distto):
    marked[u] = True
    distto[u] = 0
    queue = deque()
    queue.append(u)
    
    while len(queue) != 0:
        v = queue.popleft()
        for w in G[v]:
            if marked[w] == False:
                marked[w] = True
                edgeto[w] = v
                distto[w] = distto[v] + 1
                queue.append(w)

def hasPath(s, u, marked):
    return marked[s] == True and marked[u] == True
    
def getPath(s, u, marked, edgeto):
    if hasPath(s, u, marked) == False: return None
    
    path = []
    v = u
    while v != s:
        path.append(v)
        v = edgeto[v]
    path.append(s)
    return path

if __name__=='__main__':
    from pprint import pprint
    V = 13
    E = [ (0,1), (0,2), (0,6), (6,4), (4,3), (3,5), \
          (4,5), (7,8), (9,10), (9,11), (9,12), (11,12)]
          
    G = adjacencylist(V, E)
    marked, edgeto, distto = BreadthFirstSearch(G, 0)
    print(marked)
    print(edgeto)
    print(distto)
    path = getPath(0, 3, marked, edgeto)
    print(path)