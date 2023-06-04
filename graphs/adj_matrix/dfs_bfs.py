from collections import deque

graph = [
    [0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 1, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 0, 1, 0]
]
start_node = 3

m,n = len(graph),len(graph[0])

def dfs(graph,node):
    visited = set()
    stack = [node]
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for i in range(n):
                if graph[node][i]==1 and i not in visited:
                    stack.append(i)

def bfs(graph,node):
    q = deque()
    q.append(node)
    visited = set()
    while q:
        node = q.popleft()
        if node not in visited:
            print(node, end= " ")
            visited.add(node)
            for i in range(n):
                if graph[node][i]==1 and i not in visited:
                    q.append(i)

print("\n----DFS-----")
dfs(graph,start_node)

print("\n\n----BFS-----")
bfs(graph,start_node)

print()
