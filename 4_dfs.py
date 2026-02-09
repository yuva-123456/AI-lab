def dfs(adj, s):
    v = len(adj)
    st = [s]
    seen = [s]

    while st:
        n = st.pop()
        print(n, end=" ")
        for i in range(v-1, -1, -1):
            if adj[n][i] and i not in seen:
                seen.append(i)
                st.append(i)

adj = [
    [0,1,1,0],
    [1,0,0,1],
    [1,0,0,1],
    [0,1,1,0]
]

dfs(adj, 0)
