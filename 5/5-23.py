k = 0
for n in range(900, 1000):
    s = sorted(str(n))
    if s[0] == '0':
        if s[1] == '0':
            minim = maxim = int(s[2] + '0')
        else:
            minim = int(s[1] + '0')
            maxim = int(s[2] + s[1])
    else:
        minim = int(s[0] + s[1])
        maxim = int(s[2] + s[1])
    r = maxim - minim
    if r == 70:
        k += 1
print(k)


