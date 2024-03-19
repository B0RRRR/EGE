for n in range(1000000, 1, -1):
    s = bin(n)[2:]
    if n % 3 == 0:
        s += bin(3)[2:]
    else:
        s += '1'
    if int(s) % 5 == 0:
        s += bin(5)[2:]
    else:
        s += '1'
    if int(s, 2) < 10 ** 6:
        print(n)
        break


