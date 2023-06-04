edges = [1, 2, 0, -1]

n = len(edges)
res = -1

for node in edges:
    visited = set()
    cycle_sum = 0
    cell = node

    while cell not in visited and edges[cell] != -1:
        visited.add(cell)
        cycle_sum += cell
        cell = edges[cell]

    if edges[cell] != -1 and cell == node:
        res = max(res, cycle_sum)

print("Largest cycle sum: ", res)
