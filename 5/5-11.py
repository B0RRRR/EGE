res = []
for n in range(2, 10000):
    s = bin(n)[2:]
    s += s[-2]
    s += s[1]


    if 150 <= int(s, 2) <= 250:
        res.append(n)
print(len(res))


