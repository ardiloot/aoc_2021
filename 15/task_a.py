import numpy as np
import heapq

with open("input.txt") as fin:
    G = np.array([list(map(int, list(line.strip()))) for line in fin.readlines()], dtype=int)

dist = np.full_like(G, 1000)
pq = []
heapq.heappush(pq, (0, (0, 0)))
dist[0, 0] = 0

while len(pq) > 0:
    d0, (x0, y0) = heapq.heappop(pq)
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x0 + dx, y0 + dy
        if nx < 0 or ny < 0 or nx >= G.shape[0] or ny >= G.shape[1]:
            continue
        ndist = d0 + G[nx, ny]
        if ndist < dist[nx, ny]:
            dist[nx, ny] = ndist
            heapq.heappush(pq, (ndist, (nx, ny)))

print(dist[-1, -1])