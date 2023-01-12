# Program for å finne minste tall og tall nr i en tallrekke på 5 tall
# Ønsker å plukke ut første gang tallet forekommer ved samme tall flere ganger

minstetall = 1000
tallnr = 0

for n in range(1, 6, 1):
    print('Tall nr:', n)
    tall = int(input('Oppgi tall: '))
    if tall < minstetall:
        minstetall = tall
        tallnr = n
    else:
        if tallnr == 0:
            minstetall = tall
            tallnr = 1
    print()

print('Minste tall er', minstetall, 'og det er tall nr', tallnr, 'i rekka')
