from collections import deque

goal = '123456780'
moves = {
    0:[1,3],
    1:[0,2,4],
    2:[1,5],
    3:[0,4,6],
    4:[1,3,5,7],
    5:[2,4,8],
    6:[3,7],
    7:[4,6,8],
    8:[5,7]
}

def bfs(start):
    q = deque([(start, [])])
    visited = set()
    while q:
        state, path = q.popleft()
        if state == goal: return path + [state]
        if state in visited: continue
        visited.add(state)
        zero = state.index('0')
        for m in moves[zero]:
            new_state = list(state)
            new_state[zero], new_state[m] = new_state[m], new_state[zero]
            new_state = ''.join(new_state)
            if new_state not in visited:
                q.append((new_state, path + [state]))
    return None

solution = bfs('123405678')
if solution:
    for i, s in enumerate(solution):
        print(f"Step {i}:")
        for j in range(0,9,3):
            print(" ".join(c if c!='0' else '_' for c in s[j:j+3]))
        print("-----")
else:
    print("No solution found.")
