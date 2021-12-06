import numpy as np

counters = np.zeros((9,), dtype=np.int64)
for v in np.loadtxt("input.txt", delimiter=",", dtype=int):
    counters[v] += 1

for day in range(256):
    n = counters[0]
    counters[:-1] = counters[1:]
    counters[8] = n
    counters[6] += n
print(counters.sum())
