def water_jug_manual_path():
    jug1_capacity = int(input("Enter capacity of Jug 1: "))
    jug2_capacity = int(input("Enter capacity of Jug 2: "))
    target = int(input("Enter target amount in Jug 1: "))
    
    steps = []
    a, b = 0, 0
    steps.append((a, b))
    
    a = jug1_capacity
    steps.append((a, b))
    
    transfer = min(a, jug2_capacity - b)
    a -= transfer
    b += transfer
    steps.append((a, b))

    b = 0
    steps.append((a, b))

    transfer = min(a, jug2_capacity - b)
    a -= transfer
    b += transfer
    steps.append((a, b))

    a = jug1_capacity
    steps.append((a, b))

    transfer = min(a, jug2_capacity - b)
    a -= transfer
    b += transfer
    steps.append((a, b))

    print(f"Steps to reach ({target}, 0):")
    for idx, state in enumerate(steps):
        print(f"Step {idx}: Jug 1 = {state[0]}L, Jug 2 = {state[1]}L")

water_jug_manual_path()
