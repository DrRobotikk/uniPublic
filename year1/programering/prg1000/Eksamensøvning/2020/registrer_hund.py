def registrer_ny_hund():
    fortsette = 'j'
    while fortsette == 'j':
        bol_hundeid = False
        bol_oppdretterid = False
        bol_hundeeierid = False
        ent_hundeid = input('Oppgi hundeid: ')
        hundefil = open('hund.txt', 'r')

        hundeid = hundefil.readline()

        while hundeid != '':
            hundeid = hundeid.rstrip('\n')
            oppdretterid = hundefil.readline().rstrip('\n')
            hundeeierid = hundefil.readline().rstrip('\n')
            navn = hundefil.readline().rstrip('\n')
            kjonn = hundefil.readline().rstrip('\n')
            fodt = hundefil.readline().rstrip('\n')

            if hundeid == ent_hundeid:
                bol_hundeid = True
            hundeid = hundefil.readline()
        hundefil.close()

        if bol_hundeid == False:
            ent_oppdretterid = input('Oppgi oppdretterid: ')
            oppdretterfil = open('oppdretter.txt', 'r')

            oppdretterid = oppdretterfil.readline()

            while oppdretterid != '':
                oppdretterid = oppdretterid.rstrip('\n')
                kennelnavn = oppdretterfil.readline().rstrip('\n')
                kennelfornavn = oppdretterfil.readline().rstrip('\n')
                kenneletternavn = oppdretterfil.readline().rstrip('\n')

                if oppdretterid == ent_oppdretterid:
                    bol_oppdretterid = True
                oppdretterid = oppdretterfil.readline()
            oppdretterfil.close()
            if bol_oppdretterid == True:
                ent_hundeeierid = input('Oppgi hundeeierid: ')
                hundeeierfil = open('hundeeier.txt', 'r')

                hundeeierid = hundeeierfil.readline()

                while hundeeierid != '':
                    hundeeierid = hundeeierid.rstrip('\n')
                    fornavn = hundeeierfil.readline().rstrip('\n')
                    etternavn = hundeeierfil.readline().rstrip('\n')

                    if hundeeierid == ent_hundeeierid:
                        bol_hundeeierid = True
                    hundeeierid = hundeeierfil.readline()
                hundeeierfil.close()

                if bol_hundeid == False and bol_oppdretterid == True and bol_hundeeierid == True:
                    ent_navn = input('Oppgi navnet på hunden: ')
                    ent_kjonn = input('Oppgi kjønnet på hunden: ')
                    ent_fodt = input('Oppgi når hunden er født: ')
                    hundefil = open('hund.txt', 'a')
                    hundefil.write(ent_hundeid+'\n')
                    hundefil.write(ent_oppdretterid+'\n')
                    hundefil.write(ent_hundeeierid+'\n')
                    hundefil.write(ent_navn+'\n')
                    hundefil.write(ent_kjonn+'\n')
                    hundefil.write(ent_fodt+'\n')
                    hundefil.close()
                    print('Hunden er registrert')
        if bol_hundeid == True:
            print('Hunden er allerede registrert')
        elif bol_oppdretterid == False:
            print('Oppdretter må registreres først')
        else:
            if bol_hundeeierid == False:
                print('Hundeeir må registrees først')

        fortsette = input('Ønsker du å registre enda en hund j/n: ')


registrer_ny_hund()
