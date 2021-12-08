with open("input.txt") as fin:
    lines = fin.readlines()

res = 0
for line in lines:
    a, b = line.strip().split(" | ")
    for v in b.split():
        if len(v) in (2, 3, 4, 7):
            res += 1
print(res)
