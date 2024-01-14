s = open('24-181.txt').readline()

kmax = 0

for p in s.split('.'):
    if p.count('A') >=3:
        print(p)
        kmax = max(kmax, len(p))
        print(len(p))

print(kmax)