from functools import lru_cache
@lru_cache
def f(x, y, k):
    if x > y or x == 28: return 0
    if x == y: return 1
    count = f(x + 1, y, 1) if k != 1 else 0
    count += f(x + 3, y, 0) if x not in (8, 9) else 0
    count += f(x * 2, y, 0) if not(6 <= x <= 9) else 0
    return count
print(f(4, 93, 0))
