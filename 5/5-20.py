for n in range(10000, 99999+1):
    perv = int(str(n)[0]) + int(str(n)[2]) + int(str(n)[4])
    vtor = int(str(n)[1]) + int(str(n)[3])
    if vtor >= perv:
        s = str(perv) + str(vtor)
    else:
        s = str(vtor) + str(perv)
    if int(s) == 621:
        print(n)
        break


