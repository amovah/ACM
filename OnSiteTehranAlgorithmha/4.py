# problem: http://www.algorithmha.ir/%D9%85%D8%B3%D8%A6%D9%84%D9%87-%D8%A7%D9%84%DA%AF%D9%88%D8%B1%DB%8C%D8%AA%D9%85%DB%8C/%D9%85%D8%B3%D8%A7%D9%84%D9%87-Gholam-Simple-Game/
# solution: it's mine

def salvation(kashis, steps):
    currentPos = 0
    direction = 0
    for i in range(len(kashis)):
        if kashis[i] == 2:
            currentPos = i
            direction = 1
            break
        elif kashis[i] == 3:
            currentPos = i
            direction = -1
            break

    count = 0
    for _ in range(steps):
        currentPos = currentPos + direction
        if kashis[currentPos] == 0:
            count = count + 1
        if currentPos + 1 == len(kashis) or currentPos == 0:
            direction = direction * -1

    return count

result = []
for _ in range(int(input())):
    result.append(salvation(
        steps = int(input().split(' ')[1]),
        kashis = [int(x) for x in input().split(' ')]
    ))

for x in result:
    print(x)
