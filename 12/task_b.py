from collections import defaultdict

def solve(node):
    is_small = node[0].islower()
    cannot_use = use_count[node] > (0 if node in ("start", "end") or max(use_count.values()) > 1 else 1)
    if is_small and cannot_use:
        return 0
    if node == "end":
        return 1 
    
    res = 0   
    use_count[node] += 1 if is_small else 0
    for to in G[node]:
        res += solve(to)
    use_count[node] -= 1 if is_small else 0
    return res

G = defaultdict(list)
with open("input.txt") as fin:
    for edge in fin.readlines():
        a, b = edge.strip().split("-")
        G[a].append(b)
        G[b].append(a)
use_count = defaultdict(int)

print(solve("start"))
