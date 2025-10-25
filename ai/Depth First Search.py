graph = {
    'A': ['B', 'D'],
    'B': ['C', 'F'],
    'C': ['E', 'G', 'H'],
    'G': ['E', 'H'],
    'E': ['B', 'F'],
    'F': ['A'],
    'D': ['F'],
    'H': ['A']
}
def dfs(g, n, seen, d):
    if n not in seen:
        seen.append(n)
        if n == d:
            return seen
        for i in g[n]:
            result = dfs(g, i, seen, d)
            if result[-1] == d:
                return result
    return seen

src = input("Enter source node: ").strip().upper()
dest = input("Enter destination node: ").strip().upper()

print(dfs(graph, src, [], dest))
