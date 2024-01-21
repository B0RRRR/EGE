s = open('24-215.txt').readline()
kmax = k = 0

i = 0
while i < len(s) - 2:
    if s[i] in '123' and s[i + 1] in 'ABC' and s[i + 2] in '123':
        k += 1
        kmax = max(kmax, k)
        i += 3
    else:
        k = 0
        i += 1
print(kmax)
