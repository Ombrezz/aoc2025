grid = []

with open("day04-1.in") as f:
    grid = [line.strip() for line in f.readlines()]

def probe(x, y):
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[x]):
        return "."
    else:
        return grid[x][y]

def run_forklift():
    total = 0
    to_remove = []
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
                to_remove.append((i, j))
    for coords in to_remove:
        temp = list(grid[coords[0]])
        temp[coords[1]] = "."
        grid[coords[0]] = temp
    return total

full_total = 0
res = run_forklift()
full_total += res

while res != 0:
    res = run_forklift()
    full_total += res

print(full_total)
