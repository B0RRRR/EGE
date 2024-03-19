for n in range(1, 257):
    s = bin(n-1)[2:].zfill(8)
    
    s1 = ''
    for c in s:
        if c == '1': s1 += '0'
        else:
            s1 += '1'
    if int(s1, 2) == 143:
        print(n)
