s = open('24-s2.txt').readline()

d = {}
for i in range(len(s) - 1):
    if s[i] == 'A':
        key = s[i + 1]
        d[key] = d.get(key, 0) + 1
for x in d.items():
    if x[1] == max(d.values()):
        print(x)

