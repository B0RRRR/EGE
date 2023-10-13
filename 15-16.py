p = set(range(2, 21, 2))
q = set(range(5, 51, 5))
a = set(range(1,1000))

for x in range(1, 1000):
    if not(((x in a) <= (x in p)) and ((x in q) <= (x not in a))):
        a.remove(x)

print(len(a))







