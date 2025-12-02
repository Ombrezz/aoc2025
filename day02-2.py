from itertools import batched

ranges = []

with open("day02-1.in") as f:
    ranges = [(int(_range.split("-")[0]), int(_range.split("-")[1])) for _range in f.readline().split(",")]

total = 0

for _range in ranges:
    for i in range(_range[0], _range[1] + 1):
        n = str(i)
        for j in range(1, len(n)//2 + 1):
            test = list(batched(n, j))
            if (len(set(test)) == 1):
                total += i
                break

print(total)