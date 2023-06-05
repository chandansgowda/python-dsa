from heapq import *


def dijkstra( V, adj, S, D):
    heap = [(0,S)]
    parent = [-1]*V
    distance =[float("inf")]*V
    distance[S] = 0
    visited = set()
    while heap:
        dist, node = heappop(heap)

        if node in visited:
            continue

        visited.add(node)

        if node == D:
            path = []
            curr = node
            while curr!=S:
                path.append(curr)
                curr = parent[curr]
            path.append(S)
            path.reverse()
            print(path)


        for child, wt in adj[node]:
            new_dist = dist + wt
            if new_dist < distance[child]:
                distance[child] = new_dist
                heappush(heap, (distance[child],child))
                parent[child] = node

    return distance

adj = {
    0: [(1, 5), (2, 2)],
    1: [(3, 3)],
    2: [(1, 1), (3, 6)],
    3: [(2, 4)],
    4: [(5, 2)],
    5: [(3, 1), (4, 3)]
}
V = 6
S = 0
D = 3
distance = dijkstra( V, adj, S, D);
print(distance[D])
