fortsett = 'j'
while fortsett == 'j':

    sammenlagt = 0
    apne_fil = input('Hvilken fil skal du åpne?: ')
    try:
        tallfil = open(apne_fil, 'r')

        tall = tallfil.readline()

        while tall != '':
            tall = tall.rstrip('\n')

            sammenlagt += int(tall)
            tall = tallfil.readline()
        tallfil.close()
    except ValueError:
        print('støtte på en feil, totalen i fila så langt er:', sammenlagt)
    except IOError:
        print('Fant ikke filen du ville åpne')
    fortsett = input('ønsker du å prøve igjen j/n; ')
