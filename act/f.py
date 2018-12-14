toolpatoo = int(input().split()[1])
heyvoona = sorted([int(x) for x in input().split()])

hazfed = []
count = 0

for x in range(len(heyvoona)):
    if heyvoona[x] not in hazfed:
        count = count + 1
        for i in range(1, toolpatoo + 1):
            if len(heyvoona) - 1 >= x + i:
                if heyvoona[x + i] <= heyvoona[x] + toolpatoo:
                    hazfed.append(heyvoona[x + i])

    hazfed.append(heyvoona[x])
print(count)
