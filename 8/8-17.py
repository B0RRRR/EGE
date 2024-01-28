from itertools import product, permutations
sogl = glas = 0
k = 0
for i in range(2, 10):
    word = product('еия', repeat = i)
    for j in word:
        if j.count('е') <= 2 and j.count('и') <= 2 and j.count('я') <= 2:
            k += 1
    if i != 2:
        glas += k
    sogl += (3*k)

print(sogl+glas)




