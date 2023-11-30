def f(x, p):
    if 80 >= x >= 56 or p > 4:
        return p == 2 or p == 4
    if x > 80:
        return p == 1 or p == 3
    if p % 2:
        return f(x+1, p + 1) or f(x * 3, p + 1)
    else:
        return f(x + 1, p + 1) and f(x * 3, p + 1)

print([i for i in range(1,56) if f(i, 0)])
