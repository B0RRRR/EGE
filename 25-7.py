for i in range(2000000, 3000001):
    count = dmax = 0
    for d in range(1, round(i ** 0.5) + 1):
        if d * (i // d) == i:
            if (i // d) - d <= 120:
                count += 1
                dmax = max(dmax, i // d)
    if count >= 3:
        print(i, dmax)








