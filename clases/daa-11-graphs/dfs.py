from graph import adjacencylist

def DepthFirstSearch(G, s):
    marked = [False for _ in range(len(G))]
    edgeto = [None for _ in range(len(G))]
    dfs(G, s, marked, edgeto)
    return marked, edgeto

def dfs(G, u, marked, edgeto):
    marked[u] = True
    for v in G[u]:
        if marked[v] == False:
            edgeto[v] = u
            dfs(G, v, marked, edgeto)

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
    marked, edgeto = DepthFirstSearch(G, 0)
    print(marked)
    print(edgeto)
    path = getPath(0, 3, marked, edgeto)
    print(path)