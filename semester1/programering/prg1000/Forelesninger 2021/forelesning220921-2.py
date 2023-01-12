# Program for å finne minste tall og tall nr i en tallrekke på 5 tall

minstetall = 10**8
tallnr = 0

for n in range(1, 6, 1):
    print('Tall nr:', n)
    tall = int(input('Oppgi tall: '))
    if tall <= minstetall:
        minstetall = tall
        tallnr = n
    print()

print('Minste tall er', minstetall, 'og det er tall nr', tallnr, 'i rekka')
