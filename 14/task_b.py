import numpy as np
from collections import defaultdict

with open("input.txt") as fin:
    template = fin.readline().strip()
    fin.readline()
    substitutions = {}
    while True:
        line = fin.readline()
        if line == "":
            break
        tmp = line.strip().split(" -> ")
        substitutions[tmp[0]] = tmp[1]

pair_counts = defaultdict(int)
for j in range(len(template) - 1):
    pair_counts[template[j:j+2]] += 1

for i in range(40):
    new_pair_counts = defaultdict(int)
    for pair, count in pair_counts.items():
        if pair in substitutions:
            new_pair_counts[pair[0] + substitutions[pair]] += count
            new_pair_counts[substitutions[pair] + pair[1]] += count
        else:
            new_pair_counts[pair] += count
    pair_counts = new_pair_counts

letter_counts = defaultdict(int)
letter_counts[template[0]] += 1
letter_counts[template[-1]] += 1
for pair, count in pair_counts.items():
    letter_counts[pair[0]] += count
    letter_counts[pair[1]] += count
counts = np.array(list(letter_counts.values())) // 2
print(max(counts) - min(counts))

