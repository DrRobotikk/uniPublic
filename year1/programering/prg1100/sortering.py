usortert = [2, 1, 5, 3, 4]
bytte = 0
liste_lengde = len(usortert)
for n in range(0, liste_lengde, 1):
    if usortert[0] > usortert[1]:
        bytte = usortert[0]
        usortert[0] = usortert[1]
        usortert[1] = bytte
        print(usortert)

    if usortert[1] > usortert[2]:
        bytte = usortert[1]
        usortert[1] = usortert[2]
        usortert[2] = bytte
        print(usortert)

    if usortert[2] > usortert[3]:
        bytte = usortert[2]
        usortert[2] = usortert[3]
        usortert[3] = bytte
        print(usortert)

    if usortert[3] > usortert[4]:
        bytte = usortert[3]
        usortert[3] = usortert[4]
        usortert[4] = bytte
        print(usortert)

print(usortert)
