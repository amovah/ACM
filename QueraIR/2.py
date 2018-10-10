max = 0

for i in range(0, int(input())):
    current = input()

    if len(current) < max:
        continue;

    uniqueness = set(current)
    if len(uniqueness) > max:
        max = len(uniqueness)

print(max)
