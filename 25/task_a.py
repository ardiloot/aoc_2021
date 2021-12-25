import numpy as np

with open("input.txt") as fin:
    M = np.array([list(line.strip()) for line in fin.readlines()])

step = 0
while True:
    moved = False
    for t in [">", "v"]:
        nM = M.copy()
        for i, j in zip(*np.where(M == t)):
            if t == ">":
                ni, nj = i, (j + 1) % (M.shape[1])
            else:
                ni, nj = (i + 1) % (M.shape[0]), j
            if M[ni, nj] == ".":
                nM[i,j], nM[ni, nj] = ".", t
                moved = True
        M = nM
    step += 1
    if not moved:
        break

print(step)