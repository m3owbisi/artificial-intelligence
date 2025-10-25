from queue import Queue 

adj_list = {
    'A': ['B', 'D'],
    'B': ['C', 'F'],
    'C': ['E', 'G', 'H'],
    'G': ['E', 'H'],
    'E': ['B', 'F'],
    'F': ['A'],
    'D': ['F'],
    'H': ['A']
}

visited = {}
level = {}
parent = {}
bfs_traversal = []  
queue = Queue()

for node in adj_list.keys():
    visited[node] = False
    parent[node] = None
    level[node] = -1

source = input("Enter source node: ").strip().upper()
target = input("Enter target node: ").strip().upper()

visited[source] = True
level[source] = 0        
queue.put(source)

while not queue.empty():
    u = queue.get()
    bfs_traversal.append(u)
    for v in adj_list[u]:
        if not visited[v]:
            visited[v] = True
            parent[v] = u
            level[v] = level[u] + 1
            queue.put(v)

print("BFS traversal:", bfs_traversal)

path = []
while target is not None:
    path.append(target)
    target = parent[target]

path.reverse()
print("Shortest path is:", path)
