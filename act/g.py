input()

ls = [int(x) for x in input().split()]

answers = []

for x in range(len(ls)):
    an = []
    first = ls[x]
    maxi = -1
    count = 1
    for i in range(x + 1, len(ls)):
        count = count + 1
        if ls[i] > maxi:
            maxi = ls[i]
            an.append(count)

            if ls[i] > first:
                break

    if len(an):
        answers.append(max(an))

print(max(answers))
