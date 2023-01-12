def registrer_ny_kunde():
    ny_kunde='ja'
    while ny_kunde=='ja':
        funnet=False
        sok=input('Legg inn telefonnummret: ')
        kundefil=open('kunde.txt','r')

        telefonnr=kundefil.readline()

        while telefonnr != '':
            telefonnr=telefonnr.rstrip('\n')
            fornavn=kundefil.readline().rstrip('\n')
            etternavn=kundefil.readline().rstrip('\n')
            betalingskortnr=kundefil.readline().rstrip('\n')

            if telefonnr == sok:
                print('Kunden finnes allerede')
                funnet=True
            telefonnr=kundefil.readline()
        if not funnet == True:
            kundefil.close()
            kundefil=open('kunde.txt','a')
            fornavn=input('Oppgi fornavn: ')
            etternavn=input('Oppgi etternavn: ')
            betalingskortnr=input('Oppgi kort nummer: ')
            kundefil.write(sok+'\n'+fornavn+'\n'+etternavn+'\n'+betalingskortnr+'\n')
            kundefil.close
            print('Kunden er registrert')

        ny_kunde=input('Ønsker du å legge inn enda en kune ja/nei: ')


registrer_ny_kunde()
