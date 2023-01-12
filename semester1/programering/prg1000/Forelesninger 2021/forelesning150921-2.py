#Inndatatest i begynnelsen av programmet

#Variabel til bruk til  inndatatest, bols variabel
nytt_tall=True

#Løkke som sikrer oss gydlig verdi
while nytt_tall==True:
    #Brukeren oppgir verdi på ruletten
    tall=int(input('Hva er tallet på ruletten? '))

    #Tester om gyldig verdi
    if tall>=0 and tall<=36:
        print('gyldig verdi')
        nytt_tall=False
    else:
        print('Ugyldig verdi på ruletten, skriv inn nytt tall')

print('Da har vi fått et gyldig tall på ruletten og kan fortsette programet med å avgjøre riktig farge')

