# problem link: http://www.algorithmha.ir/%D9%85%D8%B3%D8%A6%D9%84%D9%87-%D8%A7%D9%84%DA%AF%D9%88%D8%B1%DB%8C%D8%AA%D9%85%DB%8C/%D9%85%D8%B3%D8%A6%D9%84%D9%87-column-addition/
# I only look at the problem, and didn't understand the site solution
# so I write my solution
# and it's mine

def answer(first, second, totalSum):
	first = [int(x) for x in first]
	first.reverse()
	second = [int(x) for x in second]
	second.reverse()
	totalSum = [int(x) for x in totalSum]
	totalSum.reverse()

	results = []

	firstColumn = 0
	while True:
		result = columnAddition(first, second, totalSum, firstColumn)
		results.append(result['count'])
		if result['usedColumn'] == -1:
			break
		else:
			firstColumn = result['usedColumn'] + 1

	return min(results)


def columnAddition(first, second, totalSum, firstColumn = 0):
	stack = 0
	count = firstColumn
	usedColumn = -1
	for i in range(firstColumn, len(first)):
		sum = str(first[i] + second[i])
		if len(sum) == 1:
			sum = '0' + sum
		sum = [int(x) for x in sum]
		sum.reverse()
		if (sum[0] + stack) == totalSum[i]:
			stack = sum[1]
			if usedColumn == -1:
				usedColumn = i
		else:
			count = count + 1

	return {
		'count': count,
		'usedColumn': usedColumn
	}

result = []
while(input() != '0'):
	result.append(answer(input(), input(), input()))

for x in result:
	print(x)
