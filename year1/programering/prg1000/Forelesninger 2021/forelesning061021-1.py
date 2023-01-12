# Program for å finne minste tall og tall nr i en tallrekke på 5 tall

#For å unngå å bruke dummy lar en første tall en tar imot også være minste tall
#Det gjør en i tilfelle utenfor FOR-løkka
#Ønsker å plukke ut første gang tallet forekommer ved samme tall flere ganger

print('Tall nr: 1')
tall= int(input('Oppgi tall:'))
minstetall=tall 
tallnr=1
print()


for n in range(2, 6, 1):
    print('Tall nr:', n)
    tall = int(input('Oppgi tall: '))
    if tall < minstetall:
        minstetall = tall
        tallnr = n
    print()

print('Minste tall er', minstetall, 'og det er tall nr', tallnr, 'i rekka')
