def sumFibo():
    seq = [1, 2]
    i = 2
    while True:
        current = seq[i - 1] + seq[i - 2]
        if current > 4000000:
            break;
        else:
            seq.append(current)
            i = i + 1;

    res = 0
    for i in seq:
        if i % 2 == 0:
            res  = res + i

    return res

print(sumFibo())
