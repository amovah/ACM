# problem: http://www.algorithmha.ir/%D9%85%D8%B3%D8%A6%D9%84%D9%87-%D8%A7%D9%84%DA%AF%D9%88%D8%B1%DB%8C%D8%AA%D9%85%DB%8C/%D9%85%D8%B3%D8%A7%D9%84%D9%87-%D8%AD%D8%AF%D8%B3-%DA%A9%D9%88%D9%84%D8%A7%D8%AA%D8%B2/
# I write it for my friend to learn much more
def seq(start):
	answer = 0
	if start % 2:
		answer = start * 3 + 1
	else:
		answer = start // 2

	if answer == 1:
		return 2

	return 1 + seq(answer)

def answer(beginning, ending):
	result = []
	for i in range(beginning, ending):
		result.append(seq(i))

	return max(result)

first, second = [int(x) for x in input().split()]
print(first, second, answer(first, second))
