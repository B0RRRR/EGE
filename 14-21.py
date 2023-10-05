for p in range(7, 50):
    for x in range(p):
        for y in range(p):
            if (5 * p ** 3 + x * p ** 2 + 1 * p + 6) + (x * p ** 3 + x * p ** 2 + x * p + 5) == (1 * p ** 4 + 1 * p ** 3 + 5 * p ** 2 + y * p + y):
                print(y, x, y, p)
                print(y * 15 ** 2 + x * 15 + y)




