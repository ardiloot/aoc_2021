import numpy as np

points = set()
instructions = []
with open("input.txt") as fin:
    while True:
        line = fin.readline().strip()
        if line == "":
            break
        points.add(tuple(map(int, line.strip().split(","))))

    while True:
        line = fin.readline()
        if line == "":
            break
        tmp = line.strip().split("=")
        instructions.append((0 if tmp[0][-1] == "x" else 1, int(tmp[1])))

for axis, value in instructions:
    new_points = []
    for p in points:
        if p[axis] >= value:
            new_point = list(p)
            new_point[axis] = value - (new_point[axis] - value) 
            new_points.append(tuple(new_point))
        else:
            new_points.append(p)
    points = set(new_points)
print(len(points))

indices = np.array(list(points))
M = np.full(tuple(indices.max(axis=0) + 1), ".", dtype=np.str)
for x, y in indices:
    M[x, y] = "#"
for i in range(M.shape[1]):
    print("".join(M[:, i]))
