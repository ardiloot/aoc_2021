import numpy as np

with open("input.txt") as fin:
    numbers = list(map(int, fin.readline().strip().split(",")))
    fin.readline()
    boards = []
    while True:
        boards.append([list(map(int, fin.readline().strip().split())) for _ in range(5)])
        if fin.readline() == "":
            break

boards = np.array(boards)
marked = np.zeros((len(boards), 5, 5), dtype=bool)
loser_nr = -1
for n in numbers:
    marked[boards == n] = True
    cols = marked.sum(axis=1).max(axis=1)
    rows = marked.sum(axis=2).max(axis=1)
    combined = np.maximum(rows, cols)
    if combined.min() == 5:
        sum_unmarked = boards[loser_nr][~marked[loser_nr]].sum()
        print("Result:", n * sum_unmarked)
        break   
    loser_nr = np.nonzero(combined != 5)[0][0]
