# Lager en tom liste
ansatte = []
print(ansatte)
print()

# Åpner ansattfilen og leser igjennom
ansattfil = open('laerer.txt', 'r', encoding='utf-8')

fornavn = ansattfil.readline()

while fornavn != '':
    fornavn = fornavn.rstrip('\n')
    etternavn = ansattfil.readline().rstrip('\n')
    e_post = ansattfil.readline().rstrip('\n')

    ansatte += [[fornavn, etternavn, e_post]]

    fornavn = ansattfil.readline()
ansattfil.close()

print('resultatet ble:', ansatte)
print()

print(ansatte)
print()

# Printer ut post nr 5
print(ansatte[4])
print()

# Printer et spesifikt element i en post
print(ansatte[4][2])
print()


listelengde = len(ansatte)
print(listelengde)
print()
# Skriver ut etternavnet
print('Etternavn:')
c = 1

for r in range(listelengde):
    print(ansatte[r][c])


print()

print('etternavn og e-post:')
c = 1
for r in range(listelengde):
    print(ansatte[r][c], 'har e-posten', ansatte[r][c+1])
print()
