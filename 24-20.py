from fnmatch import fnmatch

s = open('24-228.txt').readline().strip()
maxik = 0
summa = 0
proizv = 1
for p in s.split('SS'):
    if fnmatch(p, '12????77??9'):
        maxik = max(maxik, int(p))

for i in str(maxik):
    if int(i) % 2 == 0:
        proizv *= int(i)
    else:
        summa += int(i)
print(summa + proizv)