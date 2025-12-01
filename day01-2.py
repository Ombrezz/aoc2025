moves = []

with open("day1-1.in") as f:
    moves = f.readlines()

moves = [int(move[1:]) if move[0] == "R" else -int(move[1:]) for move in moves]

dial = 50

hits = 0

def sign(x):
    if x == 0:
        return 0
    return -1 if x < 0 else 1

for move in moves:
    for i in range(abs(move)):
        dial += sign(move)
        dial %= 100
        if dial == 0:
            hits += 1

print(hits)