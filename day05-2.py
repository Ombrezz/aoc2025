raw_input = []

with open("day05-1.in") as f:
    raw_input = [line.strip() for line in f.readlines()]

ranges = []
for line in raw_input:
    if "-" in line:
        ranges.append(list(map(int, line.split("-"))))
    else:
        break

ranges = sorted(ranges, key = lambda x: x[0])

for i in range(len(ranges)):
    while i < len(ranges) - 1 and ranges[i+1][0] <= ranges[i][1]:
        ranges[i][1] = max(ranges[i][1], ranges[i+1][1])
        del ranges[i+1]

total = 0

for _range in ranges:
    total += _range[1] - _range[0] + 1

print(total)