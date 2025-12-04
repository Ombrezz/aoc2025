grid = []

with open("day04-1.in") as f:
    grid = [line.strip() for line in f.readlines()]

def probe(x, y):
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[x]):
        return "."
    else:
        return grid[x][y]

total = 0

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == ".":
            continue
        count = 0
        for i_d in [-1, 0, 1]:
            for j_d in [-1, 0, 1]:
                if (i_d, j_d) == (0, 0):
                    continue
                if probe(i + i_d, j + j_d) == "@":
                    count += 1
        if count < 4:
            total += 1

print(total)