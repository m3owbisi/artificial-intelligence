def tower_of_hanoi(n,a,b,c):
    if n == 1:
        print(f"Move disk 1 from {a} to {c}")
        return
    tower_of_hanoi(n-1, a, c, b)
    print(f"Move disk {n} from {a} to {c}")
    tower_of_hanoi(n-1, b, a, c)

num_disk = int(input("Enter number of disks: "))
tower_of_hanoi(num_disk,'A','B','C')
