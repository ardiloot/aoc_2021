import numpy as np 

pos = np.loadtxt("input.txt", delimiter=",", dtype=int)
mincost = 1e9
for n in range(pos.min(), pos.max() + 1):
    steps = np.abs(pos - n)
    cost = ((steps + 1) * steps // 2).sum()
    if cost < mincost:
        mincost = cost
print(mincost)