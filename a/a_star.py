graph = { 
    "A":({'B':5,'C':7},3),
    "B":({'D':8,'E':3},2),
    "C":({'F':9},4),
    "D":({},6),
    "E":({'G':1},1),
    "F":({},5),
    "G":({},0)
}

source = input("Enter source vertex : ")
dest = input("Enter destination vertex : ")
heuristic = int(input("Enter heuristic value for source: "))

queue = {source: (heuristic, 0)}  # (heuristic, cost so far)
path = []

while queue:
    current = min(queue, key=lambda k: queue[k][0] + queue[k][1])
    path.append(current)
    
    if current == dest:
        break
    
    g_current = queue[current][1]
    
    for neighbor, cost in graph[current][0].items():
        if neighbor not in path:
            queue[neighbor] = (graph[neighbor][1], g_current + cost)
    
    del queue[current]

if path[-1] == dest:
    print("Path found:", " -> ".join(path))
else:
    print("Path not found!")
