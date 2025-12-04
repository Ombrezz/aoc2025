### UNSOLVED

banks = []

with open("day03-1.in") as f:
    banks = [line.strip() for line in f.readlines()]

total = 0

# algorithm: going from right to left, select digits in decreasing order (9s first, then 8s, etc...)
# handle second to last case to prevent smaller number from becoming first digit

length = 2
for bank in banks:
    count = 0
    selection = []
    for d in range(9, 0, -1):
        for i in range(len(bank) - 1, -1, -1):
            if count != length - 3:
                if bank[i] == str(d):
                    selection.append(i)
                    count += 1
            else:
                if bank[i] == str(d):
                    # logical implication = not(p) or q
                    if not(i < min(selection)) or d >= int(bank[min(selection)]):
                        print(count, d, i, int(bank[min(selection)]))
                        selection.append(i)
                        count += 1
            if count == length:
                break
        if count == length:
            break
    selected = ""
    while len(selection) > 0:
        to_add = min(selection)
        selected += bank[to_add]
        selection.remove(to_add)
    print(selected)
    total += int(selected)
print(total)