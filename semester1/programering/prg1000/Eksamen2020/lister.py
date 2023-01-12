#Lager en løkke for å kunne få flere utskrifter
fortsette = 'j'

while fortsette == 'j':
    #Lager en tom liste
    oppbevaringsliste = []

    #Åpner filen
    oppbevaringsfil=open('oppbevaring.txt','r')

    #Leser gjennom filen
    mobilnr = oppbevaringsfil.readline()

    while mobilnr != '':
        mobilnr=mobilnr.rstrip('\n')
        regnr=oppbevaringsfil.readline().rstrip('\n')
        innlevert=oppbevaringsfil.readline().rstrip('\n')
        utlevert=oppbevaringsfil.readline().rstrip('\n')
        hylle=oppbevaringsfil.readline().rstrip('\n')
        pris=oppbevaringsfil.readline().rstrip('\n')

        #Legger alt i lista
        oppbevaringsliste += [mobilnr]
        oppbevaringsliste += [regnr]
        oppbevaringsliste += [innlevert]
        oppbevaringsliste += [utlevert]
        oppbevaringsliste += [hylle]
        oppbevaringsliste += [pris]

        mobilnr=oppbevaringsfil.readline()
    oppbevaringsfil.close()
    
    #Ber om mobilnr å søke etter
    ent_mobilnr=input('Oppgi mobilnr: ')

    oppbevaringsliste_lengde=len(oppbevaringsliste)

    #Tester på oppgitt mobilnr for å finne elementene vi skal ha
    for n in range(0,oppbevaringsliste_lengde,1):
        if ent_mobilnr == oppbevaringsliste[n]:
            print(oppbevaringsliste[n],oppbevaringsliste[n+1],oppbevaringsliste[n+2],oppbevaringsliste[n+3])



    fortsette = input('Ønsker du ny utskrift j/n: ')