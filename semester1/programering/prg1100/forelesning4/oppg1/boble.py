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


bytte = True
stoppmerke = 1
liste_lengde = len(fornavnliste)

while bytte:
    bytte = False

    for i in range(0, liste_lengde-stoppmerke, 1):
        if fornavnliste[i] > fornavnliste[i+1]:
            bytte = True
            byttevariabel = fornavnliste[i]
            fornavnliste[i] = fornavnliste[i+1]
            fornavnliste[i+1] = byttevariabel

    stoppmerke = stoppmerke+1

print(fornavnliste)


fornavnsortert = open('fornavn_sortert2.txt', 'w')

for n in range(liste_lengde):
    fornavnsortert.write(fornavnliste[n]+'\n')


fornavnsortert.close()
