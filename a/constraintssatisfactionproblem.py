import itertools

variables = ['A', 'B', 'C']
colors = ['Red', 'Blue', 'Yellow']

all_assignments = itertools.product(colors, repeat=len(variables))

def valid(assignment):
    return len(set(assignment)) == len(assignment)

solutions = []

for assignment in all_assignments:
    if valid(assignment):
        solutions.append(dict(zip(variables, assignment)))

print("Valid colorings of A, B, C (all different):")
for sol in solutions:
    print(sol)
