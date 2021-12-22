import re
import numpy as np

cmds = []
with open("input.txt")  as fin:
    for line in fin.readlines():
        m = re.match(r"^(on|off) x=(.*)\.\.(.*),y=(.*)\.\.(.*),z=(.*)\.\.(.*)$", line)
        coords = np.array(list(map(int, m.groups()[1:])), dtype=int)
        cmds.append((m[1] == "on", coords))

xs = np.array(sorted(set([cs[0] for _, cs in cmds] + [cs[1] + 1 for _, cs in cmds])))
ys = np.array(sorted(set([cs[2] for _, cs in cmds] + [cs[3] + 1 for _, cs in cmds])))
zs = np.array(sorted(set([cs[4] for _, cs in cmds] + [cs[5] + 1 for _, cs in cmds])))

M = np.zeros((len(xs), len(ys), len(zs)), dtype=bool)
for state, (x0, x1, y0, y1, z0, z1) in cmds:
    ix0, ix1 = np.searchsorted(xs, [x0, x1 + 1])
    iy0, iy1 = np.searchsorted(ys, [y0, y1 + 1])
    iz0, iz1 = np.searchsorted(zs, [z0, z1 + 1])
    M[ix0:ix1, iy0:iy1, iz0:iz1] = state

volume = np.prod(np.meshgrid(xs[1:] - xs[:-1], ys[1:] - ys[:-1], zs[1:] - zs[:-1], indexing="ij"), axis=0, dtype=np.int64)
res = (M[:-1, :-1, :-1] * volume).sum()
print(res)