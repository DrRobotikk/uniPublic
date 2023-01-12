# Ber om ett tall mellom 1 og 12 fra brukeren
tall = int(input('Legg inn et tall mellom 1 og 12 '))
# analyserer bruker input og finner ut hvilket kvartal måneden tilhører
if tall <= 3:
    print('Måneden er i første kvartal')
else:
    if tall <= 6:
        print('Måneden er i andre kvartal')
    else:
        if tall <= 9:
            print('Måneden er i tredje kvartal')
        else:
            print('Måneden er i fjerde kvartal')
