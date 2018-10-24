# problem: http://www.algorithmha.ir/%D9%85%D8%B3%D8%A6%D9%84%D9%87-%D8%A7%D9%84%DA%AF%D9%88%D8%B1%DB%8C%D8%AA%D9%85%DB%8C/%D9%85%D8%B3%D8%A7%D9%84%D9%87-Encrypted-SMS/
# solution: it's mine.

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
