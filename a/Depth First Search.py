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

def dfs(g, node, seen, target):
    if node not in seen:
        seen.append(node)
        if node == target:
            return seen
        for neighbor in g[node]:
            result = dfs(g, neighbor, seen, target)
            if result[-1] == target:
                return result
    return seen

src = input("Enter source node: ")
dest = input("Enter destination node: ")

print(dfs(graph, src, [], dest))
