#Inndata antall km
km = float(input('Hvor mange kilometer skal du kjøre? '))

fastpris1 = 750
fastpris2 = 300+2*km
fastpris3 = 150+4*km

bestpris = 0

if fastpris1 < fastpris3 :
    bestpris = fastpris1
else:
    if fastpris2 < fastpris3:
        bestpris = fastpris2
    else:
        if fastpris3 < fastpris1:
            bestpris = fastpris3
    








    
print('Den besteprisen for deg er', bestpris)
