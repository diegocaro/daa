from digraph import adjacencylist

def TopologicalSort(G, s):
    marked = [False for _ in range(len(G))]
    postorder = []
    for v in range(len(G)):
        if not marked[v]:
            dfs(G, v, marked, postorder)
    tsort = list(reversed(postorder))
    return marked, tsort

def dfs(G, u, marked, postorder):
    marked[u] = True
    for v in G[u]:
        if not marked[v]:
            dfs(G, v, marked, postorder)
    postorder.append(u)

if __name__=='__main__':
    from pprint import pprint
    V = 7
    E = [(0,1), (0,2), (0,5), (6,0), (5,2), \
         (3,2), (3,5), (3,4), (3,6), (1,4), (6,4)]
          
    G = adjacencylist(V, E)
    marked, order = TopologicalSort(G, 0)
    print(order)