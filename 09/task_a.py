
with open("input.txt") as fin:
    m = list(map(str.strip, fin.readlines()))

res = 0
for i in range(len(m)):
    for j in range(len(m[i])):
        is_minima = True
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj
            if ni < 0 or nj < 0 or ni >= len(m) or nj >= len(m[0]):
                continue
            if m[ni][nj] <= m[i][j]:
                is_minima = False
                break
        if is_minima:
            res += int(m[i][j]) + 1
print(res) 