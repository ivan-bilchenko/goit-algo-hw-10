"""
Computes the definite integral of f(x) = x^2 using the Monte Carlo method.

Visualizes the integration area and compares the simulation result with
the analytical solution (scipy.integrate) to validate accuracy.
"""
import matplotlib.pyplot as plt
import scipy.integrate as spi
import numpy as np

def f(x: float) -> float:
    '''Function to integrate: f(x) = x^2'''
    return x ** 2

# Integration limits
A = 0  # lower limit
B = 2  # upper limit

# 1. Monte Carlo Method
N = 100000  # Number of random points
# Generate random points
x_rand = np.random.uniform(A, B, N)
y_rand = np.random.uniform(0, f(B), N) # y від 0 до f(2)=4

# Count points under the curve
points_under_curve = y_rand < f(x_rand)
count_under = np.sum(points_under_curve)

# Area of the rectangle (width * height)
RECTANGLE_AREA = (B - A) * f(B)

# Calculate the integral
monte_carlo_integral = (count_under / N) * RECTANGLE_AREA

# 2. Analytical calculation (using scipy.integrate.quad)
analytical_integral, error = spi.quad(f, A, B)

# Output results
print(f"Integral value (Monte Carlo): {monte_carlo_integral}")
print(f"Integral value (Analytical/Quad): {analytical_integral}")
print(f"Absolute error: {abs(monte_carlo_integral - analytical_integral)}")

# --- Visualization (optional, for better understanding) ---
x = np.linspace(A - 0.5, B + 0.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ax.fill_between(np.linspace(A, B), f(np.linspace(A, B)), color='gray', alpha=0.3)

# Display a small sample of points for clarity (first 500)
ax.scatter(x_rand[:500], y_rand[:500], c=points_under_curve[:500], cmap='coolwarm', s=1, alpha=0.5)

ax.set_xlim([A - 0.5, B + 0.5])
ax.set_ylim([0, f(B) + 0.5])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_title(f'Графік інтегрування f(x) = x^2 від {A} до {B}')
plt.grid()
plt.show()
