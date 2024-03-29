import numpy as np
import time
# Define the function and its derivative
def f(x):
    return (2*np.cos(x)) - (3*x)

def f_prime(x):
    return (-2*np.sin(x) - 3)

# Newton's method iteration
def newton_iteration(x):
    return x - f(x) / f_prime(x)

# Initial guess

def newton():
  x0 = np.pi/6
  x_final = 0
  for i in range(100000):
    x_final = newton_iteration(x0)
    x0 = x_final
  return x_final

# Time:
start = time.perf_counter()
print(newton())
end = time.perf_counter()
print("Elapsed = {} seconds".format((end - start)))

"""
Output:
0.5635692042255157
Elapsed = 0.5257951349994983 seconds
"""
