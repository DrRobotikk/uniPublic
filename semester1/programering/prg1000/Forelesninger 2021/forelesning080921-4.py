# Oppgave 3-9, program for å beregne farge på tall på ruletten
# Alternativ 1, nøsting av hvis setninger mtp intervall og farge

# Steg 1 avgjøre gyldig tall
# Steg2, finne riktig intervall
# Steg3, finne riktig farge for tallet i intervall

# Bruker oppgir verdi på ruletten
tall = int(input('Hva er tallet på ruletten? '))

# Tester om gyldig verdi og beregner riktig farge for gyldige verdier
if tall >= 0 and tall <= 36:
    print('Gyldig tall')

    if tall == 0:
        print('Tallet er', tall, 'og er markert "grønn" på ruletten')
    else:
        if tall <= 10:
            print('Tallet er', tall, 'og er i intervallet [1,10]')
            if (tall % 2) == 0:
                print('Tallet er partall og markert "sort" på ruletten')
            else:
                print('Tallet er oddetall og markert "rødt" på ruletten')
        else:
            if tall <= 18:
                print('tallet er', tall, 'og er i intervallet [11,18]')
                if (tall % 2) == 0:
                    print('Tallet er partall og er markert "Rødt" på ruletten')
                else:
                    print('Tallet er oddetall og er markert "Sort" på ruletten')
            else:
                if tall <= 28:
                    print('Tallet er', tall, 'og er i intervall [19,28]')
                    if (tall % 2) == 0:
                        print('Tallet er partall og er markert "Sort" på ruletten')
                    else:
                        print('Tallet er oddetall og er markert "Rødt" på ruletten')
                else:
                    if tall <= 36:
                        print('tallet er', tall, 'og er i intervall [29,36]')
                        if (tall % 2) == 0:
                            print(
                                'Tallet er partall og er markert "Rødt" på ruletten')
                        else:
                            print(
                                'Tallet er oddetall og er markert med "Sort" på ruletten')


else:
    print('Ugyldig tall')
