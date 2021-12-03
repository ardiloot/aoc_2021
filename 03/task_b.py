import numpy as np

def filter(inverse=False):
    mask = np.full((data.shape[0],), True)
    for i in range(data.shape[1]):
        common = "0" if (data[mask, i] == "0").sum() > (data[mask, i] == "1").sum() else "1"
        m = data[:, i] == common
        if inverse:
            m = ~m
        mask = (mask) & m
        if mask.sum() == 1:
            return int("".join(data[mask][0]), 2)
    return None

with open("input.txt") as fin:
    data = np.array(list(map(list, map(str.strip, fin.readlines()))))
oxygen = filter()
co2 = filter(inverse=True)
print(oxygen, co2, oxygen * co2)
