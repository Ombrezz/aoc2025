raw_input = []

with open("day05-1.in") as f:
    raw_input = [line.strip() for line in f.readlines()]

ranges = []
items = []
for line in raw_input:
    if "-" in line:
        ranges.append(list(map(int, line.split("-"))))
    elif line:
        items.append(int(line))

valid = 0

for item in items:
    for _range in ranges:
        if _range[0] <= item and item <= _range[1]:
            valid += 1
            break

print(valid)