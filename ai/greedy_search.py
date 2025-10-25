graph = { 
    "A":({'B':5,'C':7},3),
    "B":({'D':8,'E':3},2),
    "C":({'F':9},4),
    "D":({},6),
    "E":({'G':1},1),
    "F":({},5),
    "G":({},0)
}

def greedy_search_rec(graph, prev, dst, path, q):
    print("Connected nodes of current node", prev, "with h(n) values: ")
    for n in graph[prev][0]:
        if n not in path:
            q[n] = graph[n][1]
            print(n, "->", q[n])
    while q:
        mn = min(q, key=q.get)
        print("Taking minimum h(n) vertex:", mn)
        if dst == mn:
            return path + [dst]
        del q[mn]   
        new_path = greedy_search_rec(graph, mn, dst, path + [mn], q)
        if new_path:
            return new_path
    return []

source = input("Enter the source vertex: ").strip().upper()
dest = input("Enter the destination vertex: ").strip().upper()

path = greedy_search_rec(graph, source, dest, [source], {})
if path:
    print("Greedy Search Recursive Path:", " -> ".join(path))
else:
    print("Path not found!")
