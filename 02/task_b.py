import numpy as np
data = np.loadtxt("input_test.txt", dtype=[("cmd", np.object), ("value", int)])

aim, h, d = 0, 0, 0
for cmd, v in data:
    if cmd == "forward":
        h += v
        d += aim * v
    elif cmd == "down":
        aim += v
    else:
        aim -= v

print(h, d, h * d)