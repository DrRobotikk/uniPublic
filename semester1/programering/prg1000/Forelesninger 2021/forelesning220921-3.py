# Program som simulerer test av disjunksjonen/ELLER mellom to logiske utsagn

print('Vi ønsker å vurdere A>3 eller B<6 for ulike verdier av A og B forelsening 4 onsdag 8.9.2021')

# I dette eksempelet bryter vi med at variabelnavn bør skrives med små bokstaber

# verdien på A styres av en FOR-løkke fra og med verdien 2 og til verdien 5
for A in range(2, 6, 1):
    # verdien på B styres av en FOR-løkke fra og med verdien 4 til verdien 7
    for B in range(4, 8, 1):
        # Så lager vi en test på disjunksjonen
        if A > 3 or B < 6:
            print('Verdien på A er', A, 'og verdien på B er',
                  B, 'og disjunkosnen/ELLER er sann')
        else:
            print('Verdien på A er', A, 'og verdien på B er',
                  B, 'og disjunkosnen/ELLER er usann')
    print('Da er det slutt på løkka for å øke B med en')
    print()
    print('Da øker verdien på A med 1')

print('Da er det slutt på løkka for å øke A med 1, og dermed slutt på programmet')
