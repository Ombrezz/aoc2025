grid = []

with open("day07-1.in") as f:
    grid = [list(line.strip()) for line in f.readlines()]

grid = [[1 if tile == "S" else (0 if tile == "." else "^") for tile in line] for line in grid]

for i in range(len(grid) - 1):
    for j in range(len(grid[i])):
        if type(grid[i][j]) == int and grid[i][j] != 0 and grid[i+1][j] != "^":
            grid[i+1][j] += grid[i][j]
        elif type(grid[i][j]) == int and grid[i][j] != 0 and grid[i+1][j] == "^":
            grid[i+1][j-1] += grid[i][j]
            grid[i+1][j+1] += grid[i][j]

print(sum(grid[-1]))