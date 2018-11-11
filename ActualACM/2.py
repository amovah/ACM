# problem: http://www.algorithmha.ir/%D9%85%D8%B3%D8%A6%D9%84%D9%87-%D8%A7%D9%84%DA%AF%D9%88%D8%B1%DB%8C%D8%AA%D9%85%DB%8C/%D9%85%D8%B3%D8%A7%D9%84%D9%87-%D8%AD%D8%AF%D8%B3-%DA%A9%D9%88%D9%84%D8%A7%D8%AA%D8%B2/
# I write it for my friend to learn much more
memory = [0] * 100001
def seq(start):
    if 100000 >= start:
        if memory[start] != 0:
            return memory[start]

    answer = 0
    if start == 1:
        return 1

    if start % 2:
        answer = start * 3 + 1
    else:
        answer = start // 2

    inter = 1 + seq(answer)
    if 100000 >= start:
        memory[start] = inter
    return inter

def answer(beginning, ending):
    result = []
    for i in range(beginning, ending + 1):
        result.append(seq(i))

    return max(result)

result = []
voroodi = input()
while voroodi != '':
    first, second = [int(x) for x in voroodi.split()]
    if first > second:
        result.append(str(first) + ' ' + str(second) + ' ' + str(answer(second, first)))
    else:
        result.append(str(first) + ' ' + str(second) + ' ' + str(answer(first, second)))
    voroodi = input()

for x in result:
    print(x)
