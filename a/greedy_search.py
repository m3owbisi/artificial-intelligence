graph = { 
    "A":({'B':5,'C':7},3),
    "B":({'D':8,'E':3},2),
    "C":({'F':9},4),
    "D":({},6),
    "E":({'G':1},1),
    "F":({},5),
    "G":({},0)
}

def greedy_search(graph, current, target, path, q):
    for neighbor in graph[current][0]:
        if neighbor not in path:
            q[neighbor] = graph[neighbor][1]
    while q:
        mn = min(q, key=q.get)
        if mn == target:
            return path + [mn]
        del q[mn]
        new_path = greedy_search(graph, mn, target, path + [mn], q)
        if new_path:
            return new_path
    return []

source = input("Enter source vertex: ")
dest = input("Enter destination vertex: ")

path = greedy_search(graph, source, dest, [source], {})
if path:
    print("Greedy Search Path:", " -> ".join(path))
else:
    print("Path not found!")
