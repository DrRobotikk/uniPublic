# Definerer funksjonen
def dekksett_for_kunde():
    fortsette = 'j'
    while fortsette == 'j':
        # Lager lister
        kundeliste = []
        dekksettliste = []

        # Åpner og leser fila
        kundefil = open('kunde.txt', 'r')

        mobilnr_kunde = kundefil.readline()

        while mobilnr_kunde != '':
            mobilnr_kunde = mobilnr_kunde.rstrip('\n')
            fornavn = kundefil.readline().rstrip('\n')
            etternavn = kundefil.readline().rstrip('\n')
            e_post = kundefil.readline().rstrip('\n')

            # Legger filelementene inn i liste
            kundeliste += [mobilnr_kunde]
            kundeliste += [fornavn]
            kundeliste += [etternavn]
            kundeliste += [e_post]
            mobilnr_kunde = kundefil.readline()
        kundefil.close()

        # Åpner og leser gjennom fila
        dekksettfil = open('dekksett.txt', 'r')

        dekk_mobilnr = dekksettfil.readline()

        while dekk_mobilnr != '':
            dekk_mobilnr = dekk_mobilnr.rstrip('\n')
            dekk_regnr = dekksettfil.readline().rstrip('\n')

            # Legger filelemeter inn i lista
            dekksettliste += [dekk_mobilnr]
            dekksettliste += [dekk_regnr]
            dekk_mobilnr = dekksettfil.readline()
        dekksettfil.close()

        # Får lengdene på listeene
        kundeliste_lengde = len(kundeliste)
        dekksettliste_lengde = len(dekksettliste)
        # Oppgir nr det skal søkes op
        ent_mobilnr = input('Oppgi mobilnr: ')

        # Finner elementene en trenger til printen
        for m in range(0, kundeliste_lengde, 1):
            if ent_mobilnr == kundeliste[m]:
                funnet_mobil = kundeliste[m]
                for s in range(0, dekksettliste_lengde, 1):
                    if dekksettliste[s] == funnet_mobil:
                        print(
                            funnet_mobil, kundeliste[m+1], kundeliste[m+2], kundeliste[m+3], dekksettliste[s+1])

        fortsette = input('Ønsker du ny utskrift j/n: ')


dekksett_for_kunde()
