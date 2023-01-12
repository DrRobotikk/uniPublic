# Definerer funksjonen
def registrer_ny_kunde():
    fortsette = 'j'
    while fortsette == 'j':
        # Oppgir mobilnr å søke på
        ent_mobilnr = input('Oppgi mobilnr: ')

        bol_mobilnr = False

        kundefil = open('kunde.txt', 'r')

        # Leser gjennom fila og ser om vi finner det vi søker på
        mobilnr = kundefil.readline()

        while mobilnr != '':
            mobilnr = mobilnr.rstrip('\n')
            fornavn = kundefil.readline().rstrip('\n')
            etternavn = kundefil.readline().rstrip('\n')
            e_post = kundefil.readline().rstrip('\n')

            if mobilnr == ent_mobilnr:
                bol_mobilnr = True
            mobilnr = kundefil.readline()
        kundefil.close()

        # Hvis det vi søker på blir funnet finnes kunden allerede
        if bol_mobilnr == True:
            print('Kunden er allerede registrert')
        # Registrerer kunden
        else:
            ent_fornavn = input('Oppgi fornavnet: ')
            ent_etternavn = input('Oppgi etternavnet: ')
            ent_e_post = input('Oppgi E-postadressen: ')

            kundefil = open('kunde.txt', 'a')

            kundefil.write(ent_mobilnr+'\n')
            kundefil.write(ent_fornavn+'\n')
            kundefil.write(ent_etternavn+'\n')
            kundefil.write(ent_e_post+'\n')
            kundefil.close()

            ent_regnr = input('Oppgi regnr: ')
            ent_innlevert = input('Oppgi når dekkene er levert inn: ')
            ent_utlevert = input('Oppgi utlevertdato: ')
            ent_hylle = input('Oppgi hylle: ')
            ent_pris = input('Oppgi prisen: ')

            oppbevaringsfil = open('oppbevaring.txt', 'a')

            oppbevaringsfil.write(ent_mobilnr+'\n')
            oppbevaringsfil.write(ent_regnr+'\n')
            oppbevaringsfil.write(ent_innlevert+'\n')
            oppbevaringsfil.write(ent_utlevert+'\n')
            oppbevaringsfil.write(ent_hylle+'\n')
            oppbevaringsfil.write(ent_pris+'\n')
            oppbevaringsfil.close()

            dekksettfil = open('dekksett.txt', 'a')

            dekksettfil.write(ent_mobilnr+'\n')
            dekksettfil.write(ent_regnr+'\n')
            dekksettfil.close()
            print('Registrering utført')

        fortsette = input('Ønsker du ny registrering j/n: ')


registrer_ny_kunde()
