#Oppgave 3 oppgavesett 1, med nøsta hvis-settninger,tester < og starter med det laveste karakterkategori

#kandidatens poengsum som inndata fra bruker
poengsum=int(input('Oppgi kandidatens poengsum: '))

#tilordning av karakter ved nøsta hvis
if poengsum<40:
    karakter='F'
else:
    if poengsum<46:
        karakter='E'
    else:
        if poengsum<58:
            karakter='D'
        else:
            if poengsum<77:
                karakter='C'
            else:
                if poengsum<92:
                    karakter='B'
                else:
                    karakter='A'

#Skriver ut resultat
print('Ved poengsum',poengsum,'Får kandidaten karakteren',karakter)
