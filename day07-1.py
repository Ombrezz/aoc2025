grid = []

with open("day07-1.in") as f:
    grid = [list(line.strip()) for line in f.readlines()]

splits = 0

for i in range(len(grid) - 1):
    for j in range(len(grid[i])):
        if grid[i][j] == "S" and grid[i+1][j] == ".":
            grid[i+1][j] = "S"
        elif grid[i][j] == "S" and grid[i+1][j] == "^":
            grid[i+1][j-1] = "S"
            grid[i+1][j+1] = "S"
            splits += 1

print(splits)