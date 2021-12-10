
opening = "([<{"
closing = ")]>}"
points = {")": 3, "]": 57, "}": 1197, ">": 25137}

def is_corrupted(line):
    active = []
    for s in line:
        if s in opening:
            active.append(s)
        else:
            if opening.index(active.pop()) != closing.index(s):
                return s

with open("input.txt") as fin:
    lines = list(map(str.strip, fin.readlines()))

res = 0
for line in lines:
    s = is_corrupted(line)
    if s is None:
        continue
    res += points[s]
print(res)