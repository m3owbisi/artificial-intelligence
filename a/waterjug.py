def water_jug():
    jug1 = int(input("Enter capacity of Jug 1: "))
    jug2 = int(input("Enter capacity of Jug 2: "))
    target = int(input("Enter target amount in Jug 1: "))

    a, b = 0, 0
    steps = [(a, b)]

    a = jug1
    steps.append((a, b))

    b = min(a, jug2)
    a -= b
    steps.append((a, b))

    b = 0
    steps.append((a, b))

    transfer = min(a, jug2)
    a -= transfer
    b += transfer
    steps.append((a, b))

    a = jug1
    steps.append((a, b))

    transfer = min(a, jug2 - b)
    a -= transfer
    b += transfer
    steps.append((a, b))

    print(f"Steps to reach ({target}, 0):")
    for i, (x, y) in enumerate(steps):
        print(f"Step {i}: Jug 1 = {x}L, Jug 2 = {y}L")

water_jug()
