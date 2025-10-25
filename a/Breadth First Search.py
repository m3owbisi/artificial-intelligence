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

source = input("Enter source node: ")
target = input("Enter target node: ")

visited = {node: False for node in adj_list}
parent = {node: None for node in adj_list}
level = {node: -1 for node in adj_list}

bfs_traversal = []
queue = Queue()

visited[source] = True
level[source] = 0
queue.put(source)

while not queue.empty():
    current = queue.get()
    bfs_traversal.append(current)

    for neighbor in adj_list[current]:
        if not visited[neighbor]:
            visited[neighbor] = True
            parent[neighbor] = current
            level[neighbor] = level[current] + 1
            queue.put(neighbor)

print("BFS traversal:", bfs_traversal)

# Reconstruct shortest path from source to target
path = []
node = target
while node is not None:
    path.append(node)
    node = parent[node]
path.reverse()

print("Shortest path:", path)

