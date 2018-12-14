inp = input()

inp = inp.split('1')

ls = []
for x in inp:
    if x != '':
        ls.append(x)

max = 0
for x in ls:
    if len(x) > max:
        max = len(x)

print(max)
