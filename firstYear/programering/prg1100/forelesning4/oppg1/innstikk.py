fornavnliste = []
print(fornavnliste)

fornavnfil = open('fornavn.txt', 'r', encoding='utf-8')

fornavn = fornavnfil.readline()

while fornavn != '':
    fornavn = fornavn.rstrip('\n')

    fornavnliste += [fornavn]

    fornavn = fornavnfil.readline()
fornavnfil.close()

liste_lengde = len(fornavnliste)


for i in range(liste_lengde):
    indeks = i
    flyttes = 0

    while indeks > 0 and fornavnliste[indeks-1] > fornavnliste[indeks]:
        bytte = fornavnliste[indeks]
        fornavnliste[indeks] = fornavnliste[indeks-1]
        fornavnliste[indeks-1] = bytte

        flyttes = flyttes+1
        indeks = indeks-1

print(fornavnliste)


fornavnsortert = open('fornavn_sortert.txt', 'w')

for n in range(liste_lengde):
    fornavnsortert.write(fornavnliste[n]+'\n')


fornavnsortert.close()
