def f(x, p):
    if x >= 56 or p > 2:
        return p == 2
    if x > 80:
        return p == 1
    return f(x+1, p + 1) or f(x * 3, p + 1)
print([i for i in range(1,56) if f(i, 0)])
