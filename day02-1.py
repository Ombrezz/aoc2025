ranges = []

with open("day02-1.in") as f:
    ranges = [(int(_range.split("-")[0]), int(_range.split("-")[1])) for _range in f.readline().split(",")]

total = 0

for _range in ranges:
    for i in range(_range[0], _range[1] + 1):
        n = str(i)
        invalid = n[:len(n)//2] == n[len(n)//2:]
        total += i * invalid

print(total)