max = 0

for i in range(int(input())):
    current = set(input())
    if len(current) > max:
        max = len(current)

print(max)
