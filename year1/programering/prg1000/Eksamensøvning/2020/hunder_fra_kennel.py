def hunder_fra_kennel():
    fortsette = 'j'
    while fortsette == 'j':
        bol_kennel=False
        bol_hund=False
        bol_eier=False
        ent_kennel=input('Oppgi navnet på kenelen: ')
        kennelfil=open('oppdretter.txt','r')

        oppdretterid_kennel=kennelfil.readline()

        while oppdretterid_kennel != '':
            oppdretterid_kennel=oppdretterid_kennel.rstrip('\n')
            kennel_navn=kennelfil.readline().rstrip('\n')
            kennel_fornavn=kennelfil.readline().rstrip('\n')
            kennel_etternavn=kennelfil.readline().rstrip('\n')

            if kennel_navn == ent_kennel:
                bol_kennel=True
                #Må ta vare på variabel forid den får ny verdi rett under
                funnet_oppdrettid=oppdretterid_kennel
            oppdretterid_kennel=kennelfil.readline()
        kennelfil.close()

        if bol_kennel == True:
            hundefil=open('hund.txt','r')

            hundeid=hundefil.readline()

            while hundeid != '':
                hundeid=hundeid.rstrip('\n')
                oppdretterid_hund=hundefil.readline().rstrip('\n')
                hundeeierid_hund=hundefil.readline().rstrip('\n')
                navn=hundefil.readline().rstrip('\n')
                kjonn=hundefil.readline().rstrip('\n')
                fodt=hundefil.readline().rstrip('\n')

                if oppdretterid_hund == funnet_oppdrettid:
                    bol_hund=True
                hundeid=hundefil.readline()
                hundeeierfil=open('hundeeier.txt','r')
            

                hundeeierid=hundeeierfil.readline()

                while hundeeierid != '':
                    hundeeierid=hundeeierid.rstrip('\n')
                    fornavn=hundeeierfil.readline().rstrip('\n')
                    etternavn=hundeeierfil.readline().rstrip('\n')

                    if hundeeierid_hund == hundeeierid:
                        print(navn,kjonn,fodt,fornavn,etternavn)
                    hundeeierid=hundeeierfil.readline()
            hundefil.close()
            hundeeierfil.close()
            if bol_hund == False:
                print('Ingen hunder fra denne kennelen')




            



        fortsette=input('ønsker du ny utsrkift j/n: ')
hunder_fra_kennel()