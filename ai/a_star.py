graph = { 
    "A":({'B':5,'C':7},3),
    "B":({'D':8,'E':3},2),
    "C":({'F':9},4),
    "D":({},6),
    "E":({'G':1},1),
    "F":({},5),
    "G":({},0)
}

def get_min(q):
    mn = None
    for i in q:
        f_val = q[i][0] + q[i][1]  
        if mn is None or f_val < q[mn][0] + q[mn][1]:
            mn = i
    return mn

def a_star(graph, prev, dst, path, pcost, q):
    print("Connected nodes of current node", prev, "with h(n) values:")
    for n in graph[prev][0]:
        if n not in path:
            g_val = graph[prev][0][n] + pcost
            q[n] = (graph[n][1], g_val)
            print(n, "->", q[n], " f(n)=", q[n][0] + q[n][1])
    while q:
        mn = get_min(q)
        print("Selecting minimum vertex:", mn)
        if dst == mn:
            return path + [mn]
        pc = q[mn][1]
        del q[mn]
        new_path = a_star(graph, mn, dst, path + [mn], pc, q)
        if new_path:
            return new_path
    return []

source = input("Enter source vertex: ").strip().upper()
dest = input("Enter destination vertex: ").strip().upper()
heuristic = int(input("Enter given heuristic value for source: "))

path = a_star(graph, source, dest, [], 0, {source: (heuristic, 0)})
if path:
    print("Final Path:", " -> ".join(path))
else:
    print("Path not found!")
