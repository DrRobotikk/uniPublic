#numer analysator
#Få et heltall fra bruker
heltall = int(input('Legg inn et heltall '))
#Definer heltallsfunskjonene
if heltall > 0:
    print('Positiv')
    if  heltall % 2 == 0:
        print('partall')
    else:
        print('oddetall')
if heltall < 0:
    print('Negativ')
    if heltall % 2 == 0:
        print('partall')
    else:
        print('oddetall')

if heltall == 0:
    print('Null')


