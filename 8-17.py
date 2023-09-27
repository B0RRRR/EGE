from itertools import product, permutations
k = 0
slova = permutations('дейкстра', r=6)
for w in slova:
    s = ''.join(w)
    if 'йд' in s or 'йк' in s or 'йс' in s or 'йт' in s or 'йр' in s:
        k += 1
print(k)




