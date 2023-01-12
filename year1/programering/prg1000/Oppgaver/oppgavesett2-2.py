# Få bruker tall og sammenlign for å finne det minste
print('Tall nr: 1')
minste = int(input('Oppgi et tall: '))

tall_nr = 1
for n in range(1, 5, 1):
    print('Tall nr:', n+1)
    tall = int(input('Oppgi et tall: '))
    if tall <= minste:
        minste = tall
        tall_nr = n+1

print('Det minste tallet er', minste, 'og er tall nr:', tall_nr)
