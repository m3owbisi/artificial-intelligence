tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [3, 5],
    'E': [6, 9],
    'F': [1, 2],
    'G': [0, -1]
}

def minimax_alpha_beta(node, depth, alpha, beta, max_player):
    if node not in tree:  
        return node

    if isinstance(tree[node][0], int):  
        return max(tree[node]) if max_player else min(tree[node])

    if max_player:
        value = float('-inf')
        for child in tree[node]:
            value = max(value, minimax_alpha_beta(child, depth - 1, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta:
                print(f"Pruning branch at node {node}")
                break
        return value
    else:
        value = float('inf')
        for child in tree[node]:
            value = min(value, minimax_alpha_beta(child, depth - 1, alpha, beta, True))
            beta = min(beta, value)
            if beta <= alpha:
                print(f"Pruning branch at node {node}")
                break
        return value

best_score = minimax_alpha_beta('A', 3, float('-inf'), float('inf'), True)
print(f"The best Score is: {best_score}")
