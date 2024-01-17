s = open('24-197.txt').readline()

k = kmax = 0
for j in range(3):
    k = 0
    for i in range(j, len(s) - 2, 3):
        if s[i:i + 3] in ('XYX', 'XXX', 'XZX', 'YYY', 'YXY', 'YZY'):
            k += 1
            kmax = max(kmax, k)
        else:
            k = 0

print(kmax)