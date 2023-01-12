import os
def slett_hundeeier():
    fortsette = 'j'
    while fortsette == 'j':
        bol_hund=False
        bol_hundeeier=False

        ent_hundeeierid=input('Oppgi hundeeierid til den du skal slette: ')

        hundeeierfil=open('hundeeier.txt','r')
        hundeeierid=hundeeierfil.readline()

        while hundeeierid != '':
            hundeeierid=hundeeierid.rstrip('\n')
            fornavn=hundeeierfil.readline().rstrip('\n')
            etternavn=hundeeierfil.readline().rstrip('\n')

            if hundeeierid == ent_hundeeierid:
                bol_hundeeier = True
            hundeeierid=hundeeierfil.readline()
        hundeeierfil.close()

        if bol_hundeeier == True:
            hundefil=open('hund.txt','r')

            hundeid=hundefil.readline()

            while hundeid != '':
                hundeid=hundeid.rstrip('\n')
                oppdretterid=hundefil.readline().rstrip('\n')
                hundeeierid=hundefil.readline().rstrip('\n')
                navn=hundefil.readline().rstrip('\n')
                kjonn=hundefil.readline().rstrip('\n')
                fodt=hundefil.readline().rstrip('\n')

                if hundeeierid == ent_hundeeierid:
                    bol_hund=True
                hundeid=hundefil.readline()
            if bol_hundeeier == True and bol_hund == False:
                hundeeierfil=open('hundeeier.txt','r')
                tempfil=open('temp.txt','w')

                if hundeeierid != ent_hundeeierid:
                    tempfil.write(hundeeierid+'\n')
                    tempfil.write(fornavn+'\n')
                    tempfil.write(etternavn+'\n')
                hundeeierfil.close()
                tempfil.close()
                os.remove('hundeeier.txt')
                os.rename('temp.txt','hundeeier.txt')
                print('Kunden er slettet')
            if bol_hund == True:
                print('Kunden kan ikke slettes')

            
                




        fortsette=input('Ønkser du og slette flere kunder j/n: ')
slett_hundeeier()