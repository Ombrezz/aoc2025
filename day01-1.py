moves = []

with open("day1-1.in") as f:
    moves = f.readlines()

moves = [int(move[1:]) if move[0] == "R" else -int(move[1:]) for move in moves]

dial = 50

hits = 0

for move in moves:
    dial += move
    dial %= 100
    if dial == 0:
        hits += 1

print(hits)