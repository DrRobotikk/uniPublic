fortsett = True
student_liste = []
while fortsett:
    studentnr = int(input('Oppgi et studennr: '))
    fornavn = input('Oppgi et navn: ')
    studium = input('Oppgi studium: ')
    student_liste += [studentnr] + [fornavn] + [studium]

    svar = input('Ønsker du å legge inn en ny student ja eller nei: ')
    if svar == 'nei':
        fortsett = False 


liste_lengde=len(student_liste)

studnr = int(input('Oppgi et studentnr: '))
funnet = False

for indeks in range(0,liste_lengde,3):
    if studnr == student_liste[indeks]:
        funnet=True
        studenten = indeks

if funnet==True:
    print('Fullstendig informasjon er')
    print('Studnr: ',student_liste[studenten])
    print('Navn: ',student_liste[studenten+1])
    print('Studium: ',student_liste[studenten+2])
else:
    print('Ingen student er registrert med dette studentnr')



studiet = (input('Oppgi et studium: '))
funnet = False

for indeks in range(2,liste_lengde,3):
    if studiet == student_liste[indeks]:
        funnet=True
        studenten = indeks

if funnet==True:
    print('Fullstendig informasjon er om de på dette studiet er')
    print('Studnr: ',student_liste[studenten-2])
    print('Navn: ',student_liste[studenten-1])
    print('Studium: ',student_liste[studenten])
else:
    print('Ingen student er registrert ved dette studiet')





