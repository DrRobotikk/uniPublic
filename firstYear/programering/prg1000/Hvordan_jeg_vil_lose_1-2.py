# Inndata antall km
km = float(input('Hvor mange kilometer skal du kjøre? '))
# beregne totalpris
fastpris1 = 750
fastpris2 = 300+2*km
fastpris3 = 150+4*km

bestpris = 0
# sammenligner de 3 prisene og finner den laveste
if fastpris1 < fastpris2 and fastpris3:
    bestpris = fastpris1
else:
    if fastpris2 < fastpris3 and fastpris1:
        bestpris = fastpris2
    else:
        if fastpris3 < fastpris2 and fastpris1:
            bestpris = fastpris3
# Printer ut den laveste prisen
print('Den beste prisen for deg er', bestpris)
