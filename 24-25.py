k = 0
for s in open('24-164.txt'):
    if s.count('E') < 20:
        for i in s:
            k = max(k, s.rindex(i) - s.index(i))

print(k)



