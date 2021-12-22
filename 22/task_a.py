import re
import numpy as np

cmds = []
with open("input.txt")  as fin:
    for line in fin.readlines():
        m = re.match(r"^(on|off) x=(.*)\.\.(.*),y=(.*)\.\.(.*),z=(.*)\.\.(.*)$", line)
        coords = np.array(list(map(int, m.groups()[1:])), dtype=int) + 55
        cmds.append((m[1] == "on", coords))

M = np.zeros((110, 110, 110), dtype=bool)
for state, (x0, x1, y0, y1, z0, z1) in cmds:
    M[x0:x1+1, y0:y1+1, z0:z1+1] = state

print(M.sum())