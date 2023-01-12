# Oppgavesett 3 oppgave 2

student = []
print('Studenter til nå.', student)
print()

ny_student = True

while ny_student == True:
    studnr = int(input('Oppgi studentnr: '))
    student += [studnr]
    fnavn = input('Oppgi fornavn: ')
    student += [fnavn]
    studiet = input('Oppgi studium:')
    student += [studiet]
    print('Studenter til nå:', student)
    print()

    svar = input('Skal det leses inn flere studenter? ')
    if svar == 'nei':
        ny_student = False

listelengde_student = len(student)
print()
print('Lista med studenter er', student, 'og består av',
      int(listelengde_student/3), 'Registrete studenter.')
print()

# søke etter student på studentnr
studnr = int(input('Oppgi studentnr på student det sakl søkes på: '))
funnet = False

for indeks in range(0, listelengde_student, 3):
    if studnr == student[indeks]:
        funnet = True
        studenten = indeks

if funnet == True:
    print('Fullstendig informasjon om studenten er:', )
    print('Studentnr: ', student[studenten])
    print('Fornavn: ', student[studenten+1])
    print('Studium: ', student[studenten+2])
else:
    print('Ingen studenter med oppgitt studentnr er registrert')

# Prøv selv:
# 1)flytte print inn i for-løkka, alternativ løse med while
# 2) Søke etter studenter på studieprogram
