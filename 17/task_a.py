import re

def sim(x, y, vx, vy):
    if tx0 <= x <= tx1 and ty0 <= y <= ty1:
        return True, y
    if (vx > 0 and x > tx1) or (vx < 0 and x < tx0) or (vy < 0 and y < ty1):
        return False, 0
    
    dvx = (1 if vx < 0 else (-1 if vx > 0 else 0))
    ret, maxy = sim(x + vx, y + vy, vx + dvx, vy - 1)
    return ret, max(maxy, y)

with open("input.txt") as fin:
    m = re.match(r"target area: x=(.*)\.\.(.*), y=(.*)\.\.(.*)", fin.readline())
    tx0, tx1, ty0, ty1 = map(int, m.groups())

res = 0
for ivx in range(-200, 200):
    for ivy in range(-200, 200):
        ret, maxy = sim(0, 0, ivx, ivy)
        if ret:
            res = max(res, maxy)
print(res)