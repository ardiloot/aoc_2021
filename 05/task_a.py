import re
from collections import defaultdict

lines = []
with open("input.txt") as fin:
    for line in fin.readlines():
        m = re.match("^(.*),(.*) -> (.*),(.*)$", line)
        x1, y1, x2, y2 = map(int, m.groups())
        lines.append((min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)))

M = defaultdict(int)
for x1, y1, x2, y2 in lines:
    if x1 == x2:
        for y in range(y1, y2 + 1):
            M[(x1, y)] += 1
    elif y1 == y2:
        for x in range(x1, x2 + 1):
            M[(x, y1)] += 1

print(sum(1 for v in M.values() if v >= 2))