# to variable for og holde orden på minste tall og tallnr, begge settes til 0
minste = 0
tallnr = 0

# fem vilkårlige tall som inn data
t1 = int(input('Opgi tall 1: '))
t2 = int(input('Opgi tall 2: '))
t3 = int(input('Opgi tall 3: '))
t4 = int(input('Opgi tall 4: '))
t5 = int(input('Opgi tall 5: '))

# så tester vi for å ifnne mibnste tall

if t1 > t2:
    minste = t2
    tallnr = 2
else:
    minste = t1
    tallnr = 1

if minste > t3:
    minste = t3
    tallnr = 3

if minste > t4:
    misnte = t4
    tallnr = 4

if minste > t5:
    misnte = t5
    tallnr = 5

# så skriver vi ut resultatet, minste tall og tallnr

print('det minste tallet er', minste, 'og er tall nr', tallnr, 'i rekka')

# Tegn programkart
