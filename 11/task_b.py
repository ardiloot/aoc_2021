import numpy as np

with open("input.txt") as fin:
    M = np.array([list(map(int, list(line.strip()))) for line in fin.readlines()], dtype=int)

for it in range(1000):
    print("iter", it)
    M += 1
    flashes = list(zip(*np.where(M == 10)))
    i = 0
    while i < len(flashes):
        x, y = flashes[i]
        x0, x1, y0, y1 = max(x - 1, 0), min(x + 2, M.shape[0]), max(y - 1, 0), min(y + 2, M.shape[1])
        M[x0:x1, y0:y1] += 1
        nfx, nfy = np.where(M[x0:x1, y0:y1] == 10)
        flashes.extend(list(zip(nfx + x0, nfy + y0)))
        i += 1
    if len(flashes) == np.prod(M.shape):
        break
    M[M > 9] = 0
    