for n in range(1, 10000):
    s = bin(n)[2:]
    summ = s.count('1')
    if n % 2 == 0:
        s += bin(summ)[2:]
    else:
        s = '1' + s + '00'

    if int(s, 2) < 1000:
        print(n)


