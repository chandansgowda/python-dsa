from heapq import *

def prims(graph):
        visited = set()
        source = 0
        heap= [(0,source, source)]
        while heap:
            w, node, parent = heappop(heap)
            if node not in visited:
                visited.add(node)
                if node!=parent:
                    print(parent, "->", node, " : ", w)
                for child,wt in graph[node]:
                    if child not in visited:
                        heappush(heap,(wt,child,node))
graph = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (3, 8), (4, 5)],
    2: [(1, 3), (4, 7)],
    3: [(0, 6), (1, 8), (4, 9)],
    4: [(1, 5), (2, 7), (3, 9)]
}

prims(graph)
