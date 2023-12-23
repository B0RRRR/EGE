'''def pyat(b):
    thr1 = ''
    while b:
        thr1 += str(b % 5)
        b //= 5
    return thr1[::-1]'''

s = [int(x) for x in open('17-205.txt')]
numbers = []
for i in range(len(s) - 1):
    if (abs(s[i]) % 10 == 7 or abs(s[i + 1]) % 10 == 7) and abs(s[i + 1] + s[i]) % 12 == 0:
        numbers.append(s[i] + s[i + 1])

print(len(numbers), max(numbers))



