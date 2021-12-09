import numpy as np

def dfs(i, j):
    res = 1
    used[i, j] = True
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ni, nj = i + di, j + dj
        if ni < 0 or nj < 0 or ni >= len(m) or nj >= len(m[0]):
            continue
        if used[ni, nj] or m[ni][nj] == '9':
            continue
        res += dfs(ni, nj)
    return res

with open("input.txt") as fin:
    m = list(map(str.strip, fin.readlines()))

used = np.zeros((len(m), len(m[0])), dtype=bool)
sizes = []
for (i, j), u in np.ndenumerate(used):
    if u or m[i][j] == '9':
        continue
    sizes.append(dfs(i, j))
print(np.product(sorted(sizes)[-3:]))
