for n in range(1, 10000000):
    s = str(n)
    s1 = 0
    s2 = 0
    for i in s:
        if int(i) % 2 == 0:
            s1 += int(i)
    for j in range(0, len(s), 2):
        s2 += int(s[j])
    r = abs(s1 - s2)
    if r == 26:
        print(n)
        break

