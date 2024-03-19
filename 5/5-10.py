
for n in range(1, 10000):
    s = bin(n)[2:]
    if n % 2 == 0:
        s += '01'
    else:
        s += '10'

    if int(s, 2) > 97:
        print(n)
        break


