for n in range(1, 10000):
    s = bin(n)[2:]
    s1 = s[::-1]

    if n <= 500 and int(s1, 2) == 11:
        print(n)
