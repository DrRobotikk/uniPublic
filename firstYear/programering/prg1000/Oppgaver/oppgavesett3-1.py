# Lager en tom liste kaldt fornavn  for å mota fornavn

fornavn = []
stopp = "ja"

while stopp == "ja":
    navn = input('Oppgi et navn ').capitalize()
    fornavn += [navn]
    stopp = input('ønsker du å oppgi enda et navn ja eller nei ').lower()
# liste før bytting
print(fornavn)


liste_lengde = len(fornavn)

revliste = []
for n in range(liste_lengde-1, -1, -1):
    revnavn = fornavn[n]
    revliste += [revnavn]

print(revliste)


# liste etter reverse
# liste etter bytting
print(fornavn)
fornavn.reverse()
print(fornavn)
