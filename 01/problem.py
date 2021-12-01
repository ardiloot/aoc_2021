import numpy as np

values = np.loadtxt("input.txt")
print("Task 1:", ((values[1:] - values[:-1]) > 0).sum())

cumsum = np.cumsum(values)
new_values = cumsum[2:] - np.array([0] + list(cumsum[:-3]))
print("Task 2:", ((new_values[1:] - new_values[:-1]) > 0).sum())

