def f(x, y):
    return (y + 3 * x < a) or ( x > 9) or (y > 20)

for a in range(1, 1000):
    if all(f(x, y) for x in range(1,1000) for y in range(1, 1000)):
        print(a)
        break









