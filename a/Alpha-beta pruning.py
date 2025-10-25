tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [3, 5],
    'E': [6, 9],
    'F': [1, 2],
    'G': [0, -1]
}

def minimax(node, alpha, beta, max_player):
    if node not in tree:  
        return node
    if isinstance(tree[node][0], int):  
        return max(tree[node]) if max_player else min(tree[node])

    if max_player:
        value = float('-inf')
        for child in tree[node]:
            value = max(value, minimax(child, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta:
                print(f"Pruning branch at node {node}")
                break
        return value
    else:
        value = float('inf')
        for child in tree[node]:
            value = min(value, minimax(child, alpha, beta, True))
            beta = min(beta, value)
            if beta <= alpha:
                print(f"Pruning branch at node {node}")
                break
        return value

best_score = minimax('A', float('-inf'), float('inf'), True)
print("Best Score:", best_score)
