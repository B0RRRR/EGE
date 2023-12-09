s = set()
def f(x, k):
    if k == 6:
        s.add(x)
    else:
        f(x + 1, k + 1)
        f(x + 2, k + 1)
        f(x * 2, k + 1)

f(1, 0)
print(s)