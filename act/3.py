import math

vor = int(input())

maqsooms = 0

for x in range(0, vor):
    if x != 0:
        if vor % x == 0:
            maqsooms = maqsooms + x


if x == 0:
    print(0)
else:
    javab = math.log(maqsooms, 2)
    if int(javab) == javab:
        print(1)
    else:
        print(0)
