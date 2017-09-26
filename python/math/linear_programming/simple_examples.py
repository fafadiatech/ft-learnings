import pulp

# Define the problem we would like to solve
my_lp_problem = pulp.LpProblem("My LP Problem", pulp.LpMaximize)

# Define the variables 
x = pulp.LpVariable('x', lowBound=0, cat='Continuous')
y = pulp.LpVariable('y', lowBound=2, cat='Continuous')

# Objective function
my_lp_problem += 4 * x + 3 * y, "Z"

# Constraints
my_lp_problem += 2 * y <= 25 - x
my_lp_problem += 4 * y >= 2 * x - 8
my_lp_problem += y <= 2 * x - 5

# Solve the problem
my_lp_problem.solve()
print pulp.LpStatus[my_lp_problem.status]

# Find values of variables
for variable in my_lp_problem.variables():
    print "{} = {}".format(variable.name, variable.varValue)

# Print optimal value
print pulp.value(my_lp_problem.objective)