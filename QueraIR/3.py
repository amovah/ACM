stock = [int(item) for item in input().split(' ')]

for i in range(len(stock)):
    stock[i] = stock[i] % 2

while stock.count(1) > 1:
    counter = 0
    selected = -1

    for i in range(len(stock)):
        if stock[i] == 1 and counter < 2:
            stock[i] = 0
            counter = counter + 1
        elif selected == -1:
            selected = i

    stock[selected] = (stock[selected] + 1) % 2

result = []
for item in stock:
    if item:
        result.append('YES')
    else:
        result.append('NO')

print(' '.join(result))
