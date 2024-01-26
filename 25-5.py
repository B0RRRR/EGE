def simple(x):
    return all(x % d != 0 for d in range(2, round(x ** 0.5) + 1))
count = 0
maxd = 0
for i in range(125697, 190235):
    for d in range(2, round(i ** 0.5)):
        if d * (i // d) == i  and simple(d) and simple(i // d):
            print(d, i // d)
            count += 1
            maxd = max(maxd, i)


print(count, maxd)









