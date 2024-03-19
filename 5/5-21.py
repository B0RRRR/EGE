for n in range(1, 1000):
    s1 = 0
    s2 = 0
    for i in str(n):
        if int(i) % 2 == 0:
            s1 += int(i)
    for j in range(len(str(n)), 0, -2):
        s2 += int(j)
    r = abs(s1 - s2)
    if r == 26:
        print(n)
        break



