def bfs(adj, s):
    v = len(adj)
    q = [s]
    seen = [s]

    while q:
        n = q.pop(0)
        print(n, end=" ")
        for i in range(v):
            if adj[n][i] and i not in seen:
                seen.append(i)
                q.append(i)

adj = [
    [0,1,1,0],
    [1,0,0,1],
    [1,0,0,1],
    [0,1,1,0]
]

bfs(adj, 0)
