# Program for å else inn 5 tall i en liste og finne det minste tallet

# talliste definers som tom liste
talliste = []

# Utskrift av listeinnhold før fylling
print('Lista til nå', talliste)
print()

# FOR-løkke for å lese 5 tall inn i lista talliste
for indeks in range(0, 5, 1):
    print('tall nr:', indeks+1)
    listeverdi = int(input('Oppgi tall: '))
    # Innlest listeverdi legge inn i lista
    talliste += [listeverdi]
    # utskrift av liste innhold underveis/ med fylling
    print('Lista til nå:', talliste)
    print()

# Utskrift av listeinnhold og liste størrelse etter fylling
print('Hele lista er:', talliste)
liste_lengde = len(talliste)

print('Antall elemter i lista er:', liste_lengde)

# Prøv selv oppgave til neste gang
# utvid programmet til og finne minste tall og tallnr i lista

if talliste[0] < talliste[1]:
    minste = talliste[0]
    tallnr = 1
else:
    minste = talliste[1]
    tallnr = 2
if talliste[2] < minste:
    minste = talliste[2]
    tallnr = 3
if talliste[3] < minste:
    minste = talliste[3]
    tallnr = 4
if talliste[4] < minste:
    minste = talliste[4]
    tallnr = 5


print('minste tallet er ', minste, 'og er tall nr:', tallnr)
