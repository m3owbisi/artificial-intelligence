import random

Distance = [
    [10, 2, 9, 10],
    [2, 6, 6, 4],
    [9, 6, 0, 3],
    [10, 4, 3, 0]
]

def cost(tour):
    total = 0
    for i in range(len(tour)-1):
        total += Distance[tour[i]][tour[i+1]]
    total += Distance[tour[-1]][tour[0]]  # return to starting city
    return total

def neighbor(tour):
    a, b = random.sample(range(len(tour)), 2)
    tour[a], tour[b] = tour[b], tour[a]
    return tour

def hill_climb(iterations=100):
    tour = list(range(4))
    random.shuffle(tour)
    c = cost(tour)
    print("Starting tour:", tour, "Cost:", c)

    for _ in range(iterations):
        n = neighbor(tour[:])
        nc = cost(n)
        if nc < c:
            tour, c = n, nc
            print("Better tour:", tour, "Cost:", c)

    return tour, c

best_tour, best_cost = hill_climb()
print("Best tour:", best_tour)
print("Best cost:", best_cost)
