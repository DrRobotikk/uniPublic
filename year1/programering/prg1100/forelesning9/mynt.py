import random

antallKron = 0
antallMynt = 0


antallKast = int(input('Hvor mange kast skal du ha: '))

for antallGanger in range(1, antallKast+1, 1):
    if random.randint(0, 1) == 0:
        sideopp = 'Krone'
        antallKron += 1
    else:
        sideopp = 'Mynt'
        antallMynt += 1
    print('Resultatet av kast nr', antallGanger, 'ble', sideopp)
print('resultat ble', antallKron, 'antall krone og', antallMynt, 'antallmynt')
