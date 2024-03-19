def chet(x):
    a = ''
    while x:
        a += str(x % 4)
        x //= 4
    return a[::-1]

for n in range(1, 10000):
    s = chet(n)
    if n % 2 != 0:
        s = '2' + s + '11'
    else:
        s = '13' + s + '02'

    if int(s, 4) > 1000:
        print(int(s, 4))
        break


