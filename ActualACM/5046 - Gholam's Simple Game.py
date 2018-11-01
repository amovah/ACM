# link: https://icpcarchive.ecs.baylor.edu/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3047
# status: accepted

def salvation(steps, kashis):
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
		nextPos = currentPos + direction
		if nextPos == len(kashis) or nextPos < 0:
			direction = direction * -1
		currentPos = currentPos + direction
		if kashis[currentPos] == 0:
			count = count + 1

	return count

result = []
for _ in range(int(input())):
	result.append(salvation(int(input().split()[1]), [int(x) for x in input().split()]))

for x in result:
	print(x)
