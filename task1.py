"""
Optimizes production using Linear Programming (PuLP).

Maximizes the total output of 'Lemonade' and 'Fruit Juice' subject to
resource constraints (water, sugar, lemon juice, fruit puree).
"""

import pulp

# Creating a linear programming model (Maximization)
model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Decision variables (the number of products must be integer and >= 0)
lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Integer')

# Objective function: Maximize total quantity (Lemonade + Fruit Juice)
model += lemonade + fruit_juice, "Total Products"

# Resource constraints
# 1. Water: 2 units for Lemonade + 1 unit for Fruit Juice <= 100
model += 2 * lemonade + 1 * fruit_juice <= 100, "Water_Constraint"

# 2. Sugar: 1 unit for Lemonade <= 50
model += 1 * lemonade <= 50, "Sugar_Constraint"

# 3. Lemon Juice: 1 unit for Lemonade <= 30
model += 1 * lemonade <= 30, "Lemon_Juice_Constraint"

# 4. Fruit Puree: 2 units for Fruit Juice <= 40
model += 2 * fruit_juice <= 40, "Fruit_Puree_Constraint"

# Solving the model
model.solve()

# Output results
print(f"Status: {pulp.LpStatus[model.status]}")
print(f"Amount of Lemonade: {lemonade.varValue}")
print(f"Amount of Fruit Juice: {fruit_juice.varValue}")
print(f"Total amount of products: {lemonade.varValue + fruit_juice.varValue}")
