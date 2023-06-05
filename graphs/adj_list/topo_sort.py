
from collections import defaultdict, deque

def topologicalSort(graph, visited, indegree):
    queue = deque()
	
    for key in graph.keys():
        
        if indegree[key] == 0:
            queue.append(key)
            visited.add(key)
            
    print(visited)        
    while queue:
        
        node = queue.popleft()
        print(node, end=" ")
        
        for child in graph[node]:
            indegree[child]-=1
            
            if indegree[child] == 0:
                queue.append(child)
                visited.add(child)
                        
        
                    
                    
    

edges = [[1,2],[1,3],[1,7],[6,1],[6,3],[4,3],[5,3],[2,3],[4,1],[8,1],[9,7],[9,8]]
nodes = [1,2,3,4,5,6,7,8,9]

graph = defaultdict(list)
indegree = defaultdict(int)

for node in nodes:
    graph[node] = []
    indegree[node] = 0
    
for s,d in edges:
    graph[s].append(d)
    indegree[d]+=1
    
print(graph)
print(indegree)


visited = set()
topologicalSort(graph, visited, indegree)
