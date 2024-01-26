for i in range(251811, 251827):
    s = set()
    for d in range(1, round(i ** 0.5) + 1):
        if i % d == 0:
            s.add(d)
            s.add(i // d)

    if len(s) == 4:
        print(sorted(s)[2:])




