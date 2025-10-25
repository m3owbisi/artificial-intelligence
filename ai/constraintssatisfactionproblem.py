import itertools

variables = ['A', 'B', 'C']
colors = ['Red', 'Blue', 'Yellow']

all_assignments = itertools.product(colors, repeat=len(variables))

def valid(assignment):
    A, B, C = assignment
    return A != B and B != C and A != C

solutions = []

for assignment in all_assignments:
    if valid(assignment):
        solution_dict = dict(zip(variables, assignment))
        solutions.append(solution_dict)

print("Valid colorings of A, B, C (all different):")
for sol in solutions:
    print(sol)
