def f(x, y, k):
    if x > y or k > 6: return 0
    if x == y and k == 6: return 1
    return f(x + 1, y, k + 1) + f(x + 2, y, k + 1) + f(x * 2, y, k + 1)
print(f(1, 20, 0))

