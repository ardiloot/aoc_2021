import numpy as np

with open("input.txt") as fin:
    data = np.array(list(map(list, map(str.strip, fin.readlines()))))

output = []
for i in range(data.shape[1]):
    output.append("0" if (data[:, i] == "0").sum() > (data[:, i] == "1").sum() else "1")
gamma = int("".join(output), 2)
epsilon = (~gamma) & ((1 << len(output)) - 1)
print(gamma, epsilon, gamma * epsilon)