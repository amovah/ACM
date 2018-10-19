count = int(input().split(' ')[1])
numbers = [int(item) for item in input().split(' ')]

answers = []
for _ in range(count):
    question = int(input())
    result = 0
    for i in range(question):
        result = result + (numbers[i] ^ (question - i - 1))
    answers.append(result)

for answer in answers:
    print(answer)
