import numpy as np
data = np.loadtxt("input.txt", dtype=[("cmd", np.object), ("value", int)])

h, d = 0, 0
for cmd, v in data:
    if cmd == "forward":
        h += v
    elif cmd == "down":
        d += v
    else:
        d -= v

print(h, d, h * d)