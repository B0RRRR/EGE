from itertools import product, permutations

k = 0
coll = permutations('мстилав', r=5)
for i in coll:
    s = ''.join(i)
    s2 = ''
    for w in s:
        if w in 'мстлв':
            s2 += 's'
        else:
            s2 += 'g'
    if s2.count('s') > s2.count('g') and 'gg' not in s2:
        k += 1


print(k)