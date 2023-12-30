s = [int(x) for x in open('17-354.txt')]

numbers = []
min2 = min([t for t in s if abs(t) % 10 == 2])
nt = []
for i in range(len(s) - 1):
    abska = (abs(s[i]) % 10) - (abs(s[i + 1]) % 10)
    if (abs(abska) == 1) and \
            ((abs(s[i]) % 5 == 0) + (abs(s[i + 1]) % 5 == 0)) and \
            ((s[i] ** 2 + s[i + 1] ** 2) > min2 ** 2):
        numbers.append(s[i] + s[i + 1])
        if s[i] + s[i + 1] > 0:
            nt.append(s[i] + s[i + 1])

print(len(numbers), min(nt))
