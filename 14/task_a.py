import numpy as np

with open("input.txt") as fin:
    template = fin.readline().strip()
    fin.readline()
    substitutions = {}
    while True:
        line = fin.readline()
        if line == "":
            break
        tmp = line.strip().split(" -> ")
        substitutions[tmp[0]] = tmp[1]

cur = template
for i in range(10):
    new = []
    for j in range(len(cur) - 1):
        new += [cur[j], substitutions.get(cur[j] + cur[j + 1], "")]
    new.append(cur[-1])
    cur = "".join(new)

_, counts = np.unique(list(cur), return_counts=True)
print(counts.max() - counts.min())
    


        