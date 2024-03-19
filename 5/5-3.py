se = set()
for n in range(1, 1000):

    s = bin(n)[2:]
    s += str(s.count('1') % 2)
    s += str(s.count('1') % 2)
    if  210 <= int(s, 2) <= 260:
        se.add(int(s, 2))

print(len(se))
