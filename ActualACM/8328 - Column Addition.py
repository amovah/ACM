# link: https://icpcarchive.ecs.baylor.edu/index.php?option=com_onlinejudge&Itemid=8&category=825&page=show_problem&problem=6352
# status: failed

from math import inf

def answer(first, second, totalSum):
	first = [int(x) for x in first]
	second = [int(x) for x in second]
	totalSum = [int(x) for x in totalSum]

	result = inf
	firstColumn = len(first) - 1
	while True:
		currentResult = columnAddition(first, second, totalSum, firstColumn)
		if currentResult[0] < result:
			result = currentResult[0]
		if currentResult[1] == None:
			break
		else:
			firstColumn = currentResult[1] - 1

	return result


def columnAddition(first, second, totalSum, firstColumn):
	stack = 0
	count = len(first) - firstColumn - 1
	usedColumn = None
	for i in reversed(range(0, firstColumn + 1)):
		sum = first[i] + second[i] + stack

		if sum % 10 == totalSum[i]:
			stack = 0
			if sum > 9:
				stack = 1
			if usedColumn == None:
				usedColumn = i
		else:
			count = count + 1

		if i == 0 and sum > 9:
			return [inf, usedColumn]

	return [count, usedColumn]

result = []
while(input() != '0'):
	result.append(answer(input(), input(), input()))

for x in result:
	print(x)
