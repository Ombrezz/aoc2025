banks = []

with open("day03-1.in") as f:
    banks = [line.strip() for line in f.readlines()]

total = 0

for bank in banks:
    _max = 0
    for i in range(len(bank)):
        for j in range(i + 1, len(bank)):
            n = int(bank[i] + bank[j])
            _max = max(_max, n)
    total += _max

print(total)