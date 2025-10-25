print("=== Arithmetic Associative Law ===")
a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
c = int(input("Enter value for c: "))

# Addition
lhs_add = (a + b) + c
rhs_add = a + (b + c)

print(f" (a + b) + c = ({a} + {b}) + {c} = {lhs_add} ")
print(f" a + (b + c) = {a} + ({b} + {c}) = {rhs_add} ")

if lhs_add == rhs_add:
    print("Addition Associative Law holds")
else:
    print("Addition Associative Law does not hold")

# Multiplication
lhs_mul = (a * b) * c
rhs_mul = a * (b * c)

print(f" (a * b) * c = ({a} * {b}) * {c} = {lhs_mul} ")
print(f" a * (b * c) = {a} * ({b} * {c}) = {rhs_mul} ")

if lhs_mul == rhs_mul:
    print("Multiplication Associative Law holds")
else:
    print("Multiplication Associative Law does not hold")

print("\n=== Boolean Associative Law ===")
print("Enter Boolean values as: True/False, true/false, 1/0, or T/F")

def parse_bool_input(prompt):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in ['true', 't', '1', 'yes', 'y']:
            return True
        elif user_input in ['false', 'f', '0', 'no', 'n', '']:
            return False
        else:
            print("Invalid input. Please enter True/False, 1/0, T/F, or leave empty for False.")

A = parse_bool_input("Enter value for A: ")
B = parse_bool_input("Enter value for B: ")
C = parse_bool_input("Enter value for C: ")

# OR operation
lhs_or = (A or B) or C
rhs_or = A or (B or C)

print(f" (A or B) or C = ({A} or {B}) or {C} = {lhs_or} ")
print(f" A or (B or C) = {A} or ({B} or {C}) = {rhs_or} ")

if lhs_or == rhs_or:
    print("OR Boolean Associative Law holds")
else:
    print("OR Boolean Associative Law does not hold")

# AND operation
lhs_and = (A and B) and C
rhs_and = A and (B and C)

print(f" (A and B) and C = ({A} and {B}) and {C} = {lhs_and} ")
print(f" A and (B and C) = {A} and ({B} and {C}) = {rhs_and} ")

if lhs_and == rhs_and:
    print("AND Boolean Associative Law holds")
else:
    print("AND Boolean Associative Law does not hold")
