def convert (number, base):
    nbr = []
    while number > 0:
        nbr.insert(0, number % base)
        number //= base
    return nbr

otvet = 0
for N in range(1000, 9999):
    nbrs = convert(N, 10)
    M = sorted(nbrs)
    K = sorted(nbrs)
    K.reverse()
    k = 0
    m = 0
    for j in range(0, len(K)):
        k += K[len(K) - j - 1] * 10**j
    for j in range(0, len(M)):
        m += M[len(M) - j - 1] * 10**j
    R = k - m
    if R == 6174 and k == 9973:
        print(N, m, k, R)
print(otvet)
