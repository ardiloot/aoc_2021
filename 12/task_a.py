from collections import defaultdict

def solve(node):
    if node[0].islower() and use_count[node] > 0:
        return 0
    if node == "end":
        return 1 
    
    res = 0
    use_count[node] += 1
    for to in G[node]:
        res += solve(to)
    use_count[node] -= 1
    return res

G = defaultdict(list)
with open("input.txt") as fin:
    for edge in fin.readlines():
        a, b = edge.strip().split("-")
        G[a].append(b)
        G[b].append(a)
use_count = defaultdict(int)

print(solve("start"))
