from simpleai.search import CspProblem, backtrack

vars = ['a', 'b', 'c', 'd', 'e', 'f']

# Abcdef puede tener 6 valores posibles, 1, 2, 3, 4, 5, 6, donde a es el valor de hasta arriba, b y c en medio, d, e y f en la base
domains = {}
for variable in vars:
    domains[variable] = [1, 2, 3, 4, 5, 6]

# Define constraints
def constraint_function(variables, values):
    a, b, c, d, e, f = values
    leftDiagonal = a + b + d
    rightDiagonal = a + c + f
    bottomRow = d + e + f
    return leftDiagonal == 10 and rightDiagonal == 10 and bottomRow == 10

constraints = [(vars, constraint_function)]

# Define problem
problem = CspProblem(vars, domains, constraints)

# Find solution
solution = backtrack(problem)

# Print solution
if solution is not None:
    a, b, c, d, e, f = solution.values()
    print("   ", a)
    print(" ", b, " ", c)
    print(d, " ", e, " ", f)
else:
    print("No solution found.")