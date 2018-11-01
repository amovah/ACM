# link: https://icpcarchive.ecs.baylor.edu/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2096
# status: accepted

keypad = [
	['A', 'B', 'C'],
	['D', 'E', 'F'],
	['G', 'H', 'I'],
	['J', 'K', 'L'],
	['M', 'N', 'O'],
	['P', 'Q', 'R', 'S'],
	['T', 'U', 'V'],
	['W', 'X', 'Y', 'Z']
]

def decrypt(letter, i):
	status = letter.isupper()
	if status is False:
		letter = letter.upper()

	for letters in keypad:
		if letter in letters:
			count = letters.index(letter)
			if status is False:
				return letters[(count - i - 1) % len(letters)].lower()
			return letters[(count - i - 1) % len(letters)]

results = []
while True:
	voroodi = input()
	if voroodi == '#':
		break

	result = []
	for i in range(len(voroodi)):
		result.append(decrypt(voroodi[i], i))

	results.append(''.join(result))


for x in results:
	print(x)
