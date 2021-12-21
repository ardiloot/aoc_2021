
with open("input.txt") as fin:
    pos = [
        int(fin.readline().strip()[28:]) - 1,
        int(fin.readline().strip()[28:]) - 1,
    ]

score = [0, 0]
player = 0
n_dice = 0

while True:
    steps = sum(((n_dice + i) % 100) + 1 for i in range(3))
    n_dice += 3
    pos[player] = (pos[player] + steps)  % 10
    score[player] += pos[player] + 1
    if score[player] >= 1000:
        break
    player = player ^ 1

print(n_dice*score[player ^ 1])
