max = 0

for i in range(0, int(input())):
    current = set(input())
    if len(current) > max:
        max = len(current)

print(max)
