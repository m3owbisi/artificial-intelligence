from collections import deque

# Moves for empty tile
def moves(pos):
    row, col = divmod(pos, 3)
    return [pos-3 if row>0 else None, pos+3 if row<2 else None,
            pos-1 if col>0 else None, pos+1 if col<2 else None]

# BFS solver
def bfs(start, goal):
    q = deque([(start, [])])
    visited = set([start])

    while q:
        state, path = q.popleft()
        if state == goal: return path + [state]
        zero = state.index(0)
        for m in moves(zero):
            if m is not None:
                new = list(state)
                new[zero], new[m] = new[m], new[zero]
                t = tuple(new)
                if t not in visited:
                    visited.add(t)
                    q.append((t, path + [state]))
    return None

# Print nicely
def print_sol(sol):
    for i, s in enumerate(sol):
        print(f"Step {i}:")
        for j in range(0,9,3): print(s[j:j+3])
        print()

# Example
start = (1,2,3,4,0,5,6,7,8)
goal  = (1,2,3,4,5,6,7,8,0)

solution = bfs(start, goal)
solution and print_sol(solution)
