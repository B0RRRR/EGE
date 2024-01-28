from itertools import product, permutations

k = 0
coll = permutations('0123456789', r=6)
for i in coll:
    s = ''.join(i)
    s1 = ''
    for j in s:
        if j % 5 == 0:
            if int(j) % 2 == 0:
                s1 += 'ч'
            else:
                s1 += 'н'
    if 'нн' not in s and 'чч' not in s:
        k += 1


print(k)