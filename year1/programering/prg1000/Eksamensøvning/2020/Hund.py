fortsette = True
while fortsette == True:
    hundeliste = []

    hundefil = open('hund.txt', 'r')

    hundeid = hundefil.readline()

    while hundeid != '':
        hundeid = hundeid.rstrip('\n')
        oppdretterid = hundefil.readline().rstrip('\n')
        hundeeierid = hundefil.readline().rstrip('\n')
        navn = hundefil.readline().rstrip('\n')
        kjonn = hundefil.readline().rstrip('\n')
        fodt = hundefil.readline().rstrip('\n')

        hundeliste += [hundeid]
        hundeliste += [oppdretterid]
        hundeliste += [hundeeierid]
        hundeliste += [navn]
        hundeliste += [kjonn]
        hundeliste += [fodt]

        hundeid = hundefil.readline()
    hundefil.close()
    print(hundeliste)

    ent_oppdretterid = input('Oppgi oppdretterID: ')

    lengde_hundeliste = len(hundeliste)

    for n in range(0, lengde_hundeliste, 1):
        if ent_oppdretterid == hundeliste[n]:
            print(hundeliste[n-1], hundeliste[n+2],
                  hundeliste[n+3], hundeliste[n+4])
    svar = input('Ønsker du ny utskrift j/n ')
    if svar == 'n':
        fortsette = False
