def sum(n):
    result = 0

    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            result = result + i

    return result

print(sum(1000))
