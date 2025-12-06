from math import prod

raw_input = []
with open("day06-1.in") as f:
    raw_input = [line.strip().split() for line in f.readlines()]

width = len(raw_input[0])
height = len(raw_input)

total = 0

for i in range(width):
    operation = sum if raw_input[-1][i] == "+" else prod
    operands = []
    for j in range(height - 1):
        operands.append(int(raw_input[j][i]))
    total += operation(operands)

print(total)