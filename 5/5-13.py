for n in range(1, 10000):
    s = bin(n)[2:]
    if n % 2 != 0:
        s = '10' + s + '11'
    else:
        s = '1' + s + '00'

    if int(s, 2) > 1023:
        print(int(s, 2))
        break


