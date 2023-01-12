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

# Her starter utvidelse av program forelesning 220921-4
# Klargjøring for å finne minste tall, settes til første tall i lista utenfor løkka
minste_tall = talliste[0]
tallnr = 1

for index in range(1, 5, 1):
    if talliste[index] < minste_tall:
        # da er det et nytt tall som er minste tall
        minste_tall = talliste[index]
        # Tallnr i rekka er index i lista pluss 1
        tallnr = index+1

print('Det minste tallet er', minste_tall,
      'Og det er tall nr', tallnr, 'i lista')
