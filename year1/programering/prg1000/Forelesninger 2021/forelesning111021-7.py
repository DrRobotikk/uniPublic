# Program for innføring i funksjon/prosedyrer

def drommebolig():
    kjopsum = int(input('Oppgi prisen på bolig du søker lån for: '))
    egenkapital = int(input('Oppgi din egen kapital: '))
    brutto = int(input('Oppgi din bruttolønn: '))
#Beregne andre variabler
    kapital_prosent = egenkapital/kjopsum
    max_laan = brutto*5
    
#Sjekke om verdiene er gode nok for et lån
    if kapital_prosent >= 0.15 and max_laan >= kjopsum:
        print('Lånet kan bevilges')
    else:
        if kapital_prosent < 0.15:
            print('Du har for liten egen kapital for å få invilget lånet')
        if max_laan < kjopsum:
            print('Du trenger en høyere bruttolønn for å få invilget lånet')
    


def lanebevis():
    egenkapital = int(input('Oppgi din egen kapital: '))
    brutto = int(input('Oppgi din bruttolønn: '))
    max_laan = brutto*5
    kapital = egenkapital/max_laan
    
    

def main():
    fortsette = True

    while fortsette == True:
        valgt_kalkulator = int(input('Hvilken kalkulator vil du bruke ? '))
        if valgt_kalkulator == 1:
            drommebolig()
        else:
            lanebevis()
        svar = input('Ønkser du å bruke en av kalkulatorene på nytt ? ')
        if svar == 'nei':
            fortsette = False


# her kommer hovedprogrammet
main()
