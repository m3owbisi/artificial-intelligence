graph = {
    "S": {"A": 5, "B": 4},
    "A": {"C": 6, "D": 8},
    "B": {"E": 2, "G": 3},
    "C": {}, "D": {"G": 4}, "E": {}, "G": {}
}

h = {"S": 10, "A": 8, "B": 2, "C": 4, "D": 5, "E": 6, "G": 0}

def a_star(start, goal):
    open_list = {start: (h[start], 0)}   # {node: (heuristic, g_cost)}
    cost = {start: 0}                   # best g_cost found so far
    path = {start: [start]}              # paths from start

    while open_list:
        node = min(open_list, key=lambda n: sum(open_list[n]))
        h_val, g_val = open_list.pop(node)

        if node == goal:
            return path[node]

        for neigh, w in graph[node].items():
            new_cost = g_val + w
            if neigh not in cost or new_cost < cost[neigh]:
                cost[neigh] = new_cost
                open_list[neigh] = (h[neigh], new_cost)
                path[neigh] = path[node] + [neigh]

    return []

print("Path:", a_star("S", "G"))
