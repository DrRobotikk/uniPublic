liste = [5, 4, 3, 2, 1]

for n in range(0, len(liste), 1):
    print(' da starter gjennomgang ', n+1)

    for x in range(0, len(liste)-1, 1):
        if liste[x] > liste[x+1]:
            bytt = liste[x]
            liste[x] = liste[x+1]
            liste[x+1] = bytt
            print(liste)


print(liste)
