import os
def slett_kunde():
    slett_kunde='j'
    while slett_kunde=='j':
        kunde=False
        hund=False
        slett_tlfnr=input('Oppgi telefonnr på kunden du vil slette: ')
        kundefil=open('kunde.txt','r')

        mobilnr=kundefil.readline()

        while mobilnr != '':
            mobilnr=mobilnr.rstrip('\n')
            fornavn=kundefil.readline().rstrip('\n')
            etternavn=kundefil.readline().rstrip('\n')
            betalingskort=kundefil.readline().rstrip('\n')

            if mobilnr == slett_tlfnr:
                kunde=True
            mobilnr=kundefil.readline()
        mobilnr=kundefil.readline()
        kundefil.close()

        hundefil=open('hund.txt','r')

        hundeid=hundefil.readline()

        while hundeid != '':
            hundeid=hundeid.rstrip('\n')
            hundenavn=hundefil.readline().rstrip('\n')
            rase=hundefil.readline().rstrip('\n')
            eiersmobilnr=hundefil.readline().rstrip('\n')
            start_dato=hundefil.readline().rstrip('\n')

            if eiersmobilnr == slett_tlfnr:
                hund=True
            hundeid=hundefil.readline()
        hundefil.close()

        if kunde == True and hund == False:
            kundefil=open('kunde.txt','r')
            tempfil=open('temp.txt','w')

            mobilnr=kundefil.readline()

            while mobilnr != '':
                mobilnr=mobilnr.rstrip('\n')
                fornavn=kundefil.readline().rstrip('\n')
                etternavn=kundefil.readline().rstrip('\n')
                betalingskort=kundefil.readline().rstrip('\n')

                if mobilnr != slett_tlfnr:
                    tempfil.write(mobilnr+'\n')
                    tempfil.write(fornavn+'\n')
                    tempfil.write(etternavn+'\n')
                    tempfil.write(betalingskort+'\n')
                mobilnr=kundefil.readline()
            os.remove('kunde.txt')
            os.rename('temp.txt','kunde.txt')
            print('Kunden er slettet')
        if kunde == False:
            print('Kunden finnes ikke')
        if hund == True:
            print('Kunden kan ikke slettes')
        slett_kunde=input('Ønsker du å slette enda en kunde j/n: ')


       



slett_kunde()
