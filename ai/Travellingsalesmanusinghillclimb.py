import random

Distance = [
    [10, 2, 9, 10],
    [2, 6, 6, 4],
    [9, 6, 0, 3],
    [10, 4, 3, 0]
]

def get_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += Distance[tour[i]][tour[i + 1]]
    cost += Distance[tour[-1]][tour[0]]  
    return cost

def get_neighbor(tour):
    a, b = random.sample(range(len(tour)), 2)
    tour[a], tour[b] = tour[b], tour[a]
    return tour

def hill_climb():
    current = [0, 1, 2, 3]
    random.shuffle(current)
    current_cost = get_cost(current)
    print("Starting tour:", current, "Cost:", current_cost)

    for i in range(100):
        neighbor = current[:]
        neighbor = get_neighbor(neighbor)
        neighbor_cost = get_cost(neighbor)

        if neighbor_cost < current_cost:
            current = neighbor
            current_cost = neighbor_cost
            print("Better tour found:", current, "Cost:", current_cost)

    return current, current_cost

best_tour, best_cost = hill_climb()
print("Best tour:", best_tour)
print("Best cost:", best_cost)
