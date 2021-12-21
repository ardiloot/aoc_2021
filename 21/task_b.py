import itertools
import numpy as np

cache = {}

def solve(player, pos, score):
    if max(score) >= 21:
        return np.array(np.array(score) >= 21, dtype=np.int64)
   
    index = (player, tuple(pos), tuple(score))
    if index in cache:
        return cache[index]

    res = np.array([0, 0], dtype=np.int64)
    for dice in itertools.product(range(1, 4), repeat=3):
        npos, nscore = pos[:], score[:]
        npos[player] = (pos[player] + sum(dice)) % 10
        nscore[player] += npos[player] + 1
        res += solve(player ^ 1, npos, nscore)
    cache[index] = res
    return res

with open("input.txt") as fin:
    pos = [
        int(fin.readline().strip()[28:]) - 1,
        int(fin.readline().strip()[28:]) - 1,
    ]

print(solve(0, pos, [0, 0]).max())