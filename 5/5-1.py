for n in range(1, 1000):
    s = bin(n)[2:]
    s += str(s.count('1') % 2)
    s += str(s.count('1') % 2)
    if int(s, 2) > 137:
        print(n)
        break
