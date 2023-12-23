
def pyat(b):
    thr1 = ''
    while b:
        thr1 += str(b % 5)
        b //= 5
    return thr1[::-1]

s = [int(x) for x in open('17-4.txt')]
print(s)

numbers = []
for i in s:
    if bin(i)[2:] == '1001' and str(pyat(i))[-2:] == '11':
        numbers.append(i)

print(sum(numbers), max(numbers))



