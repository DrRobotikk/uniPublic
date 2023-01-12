def registrer_ny_hund():
    ny_hund='j'
    while ny_hund == 'j':
        
        funnet=False
        oppgitt_hundeid=input('Oppgi hundeid: ')

        hundefil=open('hund.txt','r')

        hundeid=hundefil.readline()

        while hundeid != '':
            hundeid=hundeid.rstrip('\n')
            hundenavn=hundefil.readline().rstrip('\n')
            rase=hundefil.readline().rstrip('\n')
            eiers_mobilnr=hundefil.readline().rstrip('\n')
            start_dato=hundefil.readline().rstrip('\n')

            if hundeid == oppgitt_hundeid:
                print('Voffen er allerende registrert')
                funnet=True
            hundeid=hundefil.readline()
        if not funnet:
            hundefil.close()
            oppgitt_hundenavn=input('Oppgi hundenavn: ')
            oppgitt_rase=input('Oppgi rase: ')
            oppgitt_mobilnr=input('Oppgi mobilnr: ')
            oppgitt_dato=input('Oppgi dato: ')

            kundefil=open('kunde.txt','r')
            funnet2=False
            mobilnr=kundefil.readline()

            while mobilnr != '':
                mobilnr=mobilnr.rstrip('\n')
                fornavn=kundefil.readline().rstrip('\n')
                etternavn=kundefil.readline().rstrip('\n')
                betalingskort=kundefil.readline().rstrip('\n')

                if mobilnr== oppgitt_mobilnr:
                    hundefil=open('hund.txt','a')
                    hundefil.write(oppgitt_hundeid+'\n'+oppgitt_hundenavn+'\n'+oppgitt_rase+'\n'+oppgitt_mobilnr+'\n'+oppgitt_dato+'\n')
                    hundefil.close()
                    print('Hunden er registrert')
                    funnet2=True
                mobilnr=kundefil.readline()
            kundefil.close()
            if not funnet2:
                print('du må registrere deg som kunde først')
        ny_hund=input('skal du legge til enda en hund j/n: ')

registrer_ny_hund()
            
