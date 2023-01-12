# Program for innføring i funksjon/prosedyrer

def drommebolig():
    # Her kommer kode for kalkulator 1
    print('DU har valgt kalkulator 1, Drømmebolig')
    print()


def lanebevis():
    # Her kommer kode for kalkulator 2, Lånebevis
    print('Du har valgt kalkulator 2, Lånebevis')
    print()


# Her kommer koden for programmet
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
