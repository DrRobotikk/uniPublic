#Lager funksjonen
def hunder_fra_kennel():
    fortsette = 'j'
    while fortsette == 'j':
        # Lager de forskjellige listene
        oppdretter_liste = []
        hundeliste = []
        hundeeierliste = []
        # Leser gjennom fil og legger inn i liste
        oppdretterfil = open('oppdretter.txt', 'r')

        oppdretterid_oppdrett = oppdretterfil.readline()

        while oppdretterid_oppdrett != '':
            oppdretterid_oppdrett = oppdretterid_oppdrett.rstrip('\n')
            kennelnavn = oppdretterfil.readline().rstrip('\n')
            kennelfornavn = oppdretterfil.readline().rstrip('\n')
            kenneletternavn = oppdretterfil.readline().rstrip('\n')

            oppdretter_liste += [oppdretterid_oppdrett]
            oppdretter_liste += [kennelnavn]
            oppdretter_liste += [kennelfornavn]
            oppdretter_liste += [kenneletternavn]

            oppdretterid_oppdrett = oppdretterfil.readline()
        oppdretterfil.close()

        # Leser gjennom fil og legger inn i liste
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

        # Leser gjennom fil og legger inn i liste
        hundeeierfil = open('hundeeier.txt', 'r')

        hundeeierid = hundeeierfil.readline()

        while hundeeierid != '':
            hundeeierid = hundeeierid.rstrip('\n')
            fornavn = hundeeierfil.readline().rstrip('\n')
            etternavn = hundeeierfil.readline().rstrip('\n')

            hundeeierliste += [hundeeierid]
            hundeeierliste += [fornavn]
            hundeeierliste += [etternavn]

            hundeeierid = hundeeierfil.readline()
        hundeeierfil.close()

        # Lager variabler for listelengder
        oppdretter_liste_lengde = len(oppdretter_liste)
        hundeliste_lengde = len(hundeliste)
        hundeeierliste_lengde = len(hundeeierliste)
        bol_kennelnavn = False
        bol_hundeid = False

        # Går gjennom listene for å hente ut de elemente en skal ha
        ent_kennelnavn = input('Oppgi kennelnavn: ')
        for o in range(0, oppdretter_liste_lengde, 1):
            if ent_kennelnavn == oppdretter_liste[o]:
                oppdretterid_fra_liste = oppdretter_liste[o-1]
                bol_kennelnavn = True

        if bol_kennelnavn == True:
            for h in range(0, hundeliste_lengde, 1):
                if oppdretterid_fra_liste == hundeliste[h]:
                    bol_hundeid = True
                    for e in range(0, hundeeierliste_lengde, 1):
                        if hundeliste[h+1] == hundeeierliste[e]:
                            print(hundeliste[h-1], hundeliste[h+2], hundeliste[h+3],
                                  hundeliste[h+4], hundeeierliste[e+1], hundeeierliste[e+2])

        
        if bol_kennelnavn == False:
            print('kennelen finnes ikke')
        if bol_hundeid == False:
            print('Ingen hunder er registrert på denne kennelen')

        fortsette = input('Ønsker du ny utskrift j/n: ')


hunder_fra_kennel()
