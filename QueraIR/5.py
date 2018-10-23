# problem link: http://www.algorithmha.ir/%D9%85%D8%B3%D8%A6%D9%84%D9%87-%D8%A7%D9%84%DA%AF%D9%88%D8%B1%DB%8C%D8%AA%D9%85%DB%8C/%D9%85%D8%B3%D8%A6%D9%84%D9%87-column-addition/
# I only look at the problem, and didn't understand the site solution
# so I write my solution
# and it's mine

def answer(first, second, totalSum):
    first = [int(x) for x in str(first)]
    first.reverse()
    second = [int(x) for x in str(second)]
    second.reverse()
    totalSum = [int(x) for x in str(totalSum)]
    totalSum.reverse()


    stack = 0
    count = 0
    for i in range(len(first)):
        sum = str(first[i] + second[i])
        if len(sum) == 1:
            sum = '0' + sum
        sum = [int(x) for x in sum]
        sum.reverse()

        if (sum[0] + stack) == totalSum[i]:
            stack = sum[1]
        else:
            count = count + 1


    return count

result = []
while(input() != '0'):
    result.append(answer(int(input()), int(input()), int(input())))

for x in result:
    print(x)
