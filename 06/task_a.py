import numpy as np

timers = list(np.loadtxt("input_test.txt", delimiter=",", dtype=int))

for day in range(18):
    n = len(timers)
    for i in range(n):
        if timers[i] == 0:
            timers.append(8)
            timers[i] = 6
        else:
            timers[i] -= 1
    
print(len(timers))
