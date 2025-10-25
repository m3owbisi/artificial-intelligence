def tower_of_hanoi(n, a, b, c):
    if n == 1:
        print(f"Move 1st disk from {a} to {c}")
        return
    tower_of_hanoi(n - 1, a, c, b)
    print(f"Move {n}th disk from {a} to {c}")
    tower_of_hanoi(n - 1, b, a, c)


# Example run
tower_of_hanoi(2, "A", "B", "C")
