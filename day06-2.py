from math import prod

raw_input = []
with open("day06-1.in") as f:
    raw_input = [line[:-1] for line in f.readlines()]

r_width = len(raw_input[0])
r_height = len(raw_input)

seps = [0]
for i in range(r_width):
    if all([raw_input[j][i] == " " for j in range(r_height)]):
        seps.append(i)

for h in range(r_height):
    # https://stackoverflow.com/a/10851479
    raw_input[h] = [raw_input[h][i:j] for i,j in zip(seps, seps[1:]+[None])]
    raw_input[h] = [s[1:] if i > 0 else s for i, s in enumerate(raw_input[h])]
    raw_input[-1] = list(map(lambda x: x[0], raw_input[-1]))

width = len(raw_input[0])
height = len(raw_input)

total = 0

for i in range(width):
    operation = sum if raw_input[-1][i] == "+" else prod
    raw_operands = []
    for j in range(height - 1):
        raw_operands.append(raw_input[j][i])
    operands = [""] * len(raw_operands[0])
    for k in range(len(raw_operands)):
        for l in range(len(raw_operands[k])):
            operands[l] += raw_operands[k][l]
    operands = map(int, operands)
    total += operation(operands)

print(total)