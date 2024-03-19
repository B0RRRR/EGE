for n in range(1, 10000):
    s = bin(n)[2:]
    if s.count('1') % 2 == 0:
        s += '0'
        s = '10' + s[2:]
    else:
        s += '1'
        s = '11' + s[2:]

    if int(s, 2) >= 16:
        print(n)
        break


