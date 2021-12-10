
opening = "([<{"
closing = ")]>}"
points = {")": 1, "]": 2, "}": 3, ">": 4}

def is_incomplete(line):
    active = []
    for s in line:
        if s in opening:
            active.append(s)
        else:
            if opening.index(active.pop()) != closing.index(s):
                return None
    return [closing[opening.index(s)] for s in active[::-1]]
    

with open("input.txt") as fin:
    lines = list(map(str.strip, fin.readlines()))

scores = []
for line in lines:
    missing = is_incomplete(line)
    if missing is None:
        continue
    score = 0
    for s in missing:
        score = 5 * score + points[s]
    scores.append(score)
scores.sort()
print(scores[len(scores) // 2])