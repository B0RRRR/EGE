s = open('24-264.txt').readline()
k = kmax = 1
for c in 'QWERTYUIOPLKJHGFDSAZXCVBNM':
    s = s.replace(c, '*')
for x in '0987654321':
    s = s.replace(x, 'c')

for i in range(len(s) - 1):
    if s[i:i+2] not in '**' and s[i:i+2] not in 'cc':
        k += 1
        kmax = max(kmax, k)
        print(s[i:i+2])
    else:
        k = 1
print(kmax)

