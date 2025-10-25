from collections import deque

# Each state: (M_left, C_left, Boat_side, M_right, C_right)
# Boat_side: 0 = left, 1 = right

def is_valid(m_left, c_left, m_right, c_right):
    # No negative values
    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
        return False
    # Missionaries never outnumbered by cannibals
    if m_left > 0 and m_left < c_left:
        return False
    if m_right > 0 and m_right < c_right:
        return False
    return True

def bfs():
    start = (3, 3, 0, 0, 0)  # 3 missionaries, 3 cannibals, boat left
    goal = (0, 0, 1, 3, 3)   # all on right

    q = deque()
    q.append((start, [start]))
    visited = set([start])

    moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]  # possible boat moves

    while q:
        (m_left, c_left, boat, m_right, c_right), path = q.popleft()

        if (m_left, c_left, boat, m_right, c_right) == goal:
            return path

        for m, c in moves:
            if boat == 0:  # Boat on left
                new_state = (m_left - m, c_left - c, 1, m_right + m, c_right + c)
            else:  # Boat on right
                new_state = (m_left + m, c_left + c, 0, m_right - m, c_right - c)

            if is_valid(new_state[0], new_state[1], new_state[3], new_state[4]) and new_state not in visited:
                visited.add(new_state)
                q.append((new_state, path + [new_state]))
    return None

def print_solution(solution):
    print("\nMissionaries and Cannibals Solution:\n")
    for step, (m_left, c_left, boat, m_right, c_right) in enumerate(solution):
        boat_side = "Left" if boat == 0 else "Right"
        print(f"Step {step}:")
        print(f"  Left Bank : M={m_left}, C={c_left} {'<--Boat' if boat==0 else ''}")
        print(f"  Right Bank: M={m_right}, C={c_right} {'<--Boat' if boat==1 else ''}")
        print()

# Run BFS
solution = bfs()
if solution:
    print_solution(solution)
else:
    print("No solution.")
