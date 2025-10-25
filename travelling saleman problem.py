import numpy as np
from python_tsp.exact import solve_tsp_dynamic_programming

# Cost matrix (square matrix)
distance_matrix = np.array([
    [0, 2, 9, 10],
    [1, 0, 6, 4],
    [15, 7, 0, 8],
    [6, 3, 12, 0]
])

# Solve TSP
permutation, distance = solve_tsp_dynamic_programming(distance_matrix)

print("Shortest Path:", permutation)
print("Total Distance:", distance)
