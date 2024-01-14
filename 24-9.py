s =  'Z' + open('24-1.txt').readline() + 'Z'
for c in 'ABX':
    s = s.replace(c, '*')

kmax = 0

a = [i for i in range(len(s)) if s[i] == '*']
for i in range(len(a) - 6):
    kmax = max(kmax, a[i + 6] - a[i] - 1)

print(kmax)