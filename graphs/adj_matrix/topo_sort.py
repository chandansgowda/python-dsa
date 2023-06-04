def topo_sort(graph):
    m,n=len(graph),len(graph[0])
    res = []
    visited = [0] * m

    def dfs(node):
        visited[node] = 1
        for i in range(n):
            if graph[node][i] and not visited[i]:
                dfs(i)
        res.append(node)

    for i in range(m):
        if not visited[i]:
            dfs(i)

    res.reverse()
    return res


graph = [
    [0, 1, 0, 0, 1],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0]
]

print(topo_sort(graph))
