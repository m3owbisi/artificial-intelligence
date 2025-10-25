print("=== Arithmetic Distributive Law ===")
a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
c = int(input("Enter value for c: "))

lhs = a * (b + c)
rhs = (a * b) + (a * c)

print(f" LHS = {a} * {b} + {c}) = {lhs} ")
print(f" RHS = ({a} * {b}) + ({a} * {c}) = {rhs} ")

if lhs == rhs:
    print("Distributive Law holds for arithmetic!/n")
else:
    print("Not equal")

print("=== Boolean Distributive Law ===")
A = bool(input("Enter value for A: "))
B = bool(input("Enter value for B: "))
C = bool(input("Enter value for C: "))

lhs_bool = A and (B or C)
rhs_bool = (A and B) or (A and C)

print(f"LHS = {A} and ({B} or {C}) = {lhs_bool} ")
print(f"RHS = {A} or ({B} or {C}) = {rhs_bool} ")

if lhs_bool == rhs_bool:
    print("Distributive Law holds for Boolean Logic!")
else:
    print("Not equal")
