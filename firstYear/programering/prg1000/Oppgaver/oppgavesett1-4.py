# Finn det minste talle
tall1 = int(input('Legg inn et tall '))
tall2 = int(input('Legg inn et tall '))
tall3 = int(input('Legg inn et tall '))
tall4 = int(input('Legg inn et tall '))
tall5 = int(input('Legg inn et tall'))


if tall1 < tall2:
    minst = tall1
    tallnr = 1
else:
    minst = tall2
    tallnr = 2
if tall3 < minst:
    minst = tall3
    tallnr = 3
if tall4 < minst:
    minst = tall4
    tallnr = 4
if tall5 < minst:
    minst = tall5
    tallnr = 5

print('Det minste tallet er', minst, 'og tall numret er', tallnr)
