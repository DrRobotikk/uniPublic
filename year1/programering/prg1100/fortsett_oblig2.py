

def skriv_karakterliste(skriv_karakterlisteStudentnr):
    funnet_resultat = False

    studentfil = open('student.txt', 'r')

    studentnr = studentfil.readline()

    while studentnr != '':
        studentnr = studentnr.rstrip('\n')
        fornavn = studentfil.readline().rstrip('\n')
        etternavn = studentfil.readline().rstrip('\n')
        studium = studentfil.readline().rstrip('\n')

        if studentnr == skriv_karakterlisteStudentnr:
            print(fornavn, etternavn, studium)

        studentnr = studentfil.readline()
    studentfil.close()
    print()

    eksamensfil = open('eksamensresultat.txt', 'r')
    emnekode = eksamensfil.readline()
    while emnekode != '':
        emnekode = emnekode.rstrip('\n')
        studentnr = eksamensfil.readline().rstrip('\n')
        karakter = eksamensfil.readline().rstrip('\n')

        if studentnr == skriv_karakterlisteStudentnr:
            funnet_resultat = True
            emnefil = open('emne.txt', 'r')
            emne = emnefil.readline()

            while emne != '':
                emne = emne.rstrip('\n')
                emnenavn = emnefil.readline().rstrip('\n')

                if emne == emnekode:
                    print(emnekode, emnenavn, karakter)
                emne = emnefil.readline()
            emnefil.close()
        emnekode = eksamensfil.readline()
    eksamensfil.close()

    if funnet_resultat == False:
        print('Studentenen har ikke resultater ')


def sjekk_student():
    funnet_student = False

    oppgitt_studentnr = input('Oppgi et studentnr: ')

    studentfil = open('student.txt', 'r')

    studentnr = studentfil.readline()

    while studentnr != '':
        studentnr = studentnr.rstrip('\n')
        fornavn = studentfil.readline().rstrip('\n')
        etternavn = studentfil.readline().rstrip('\n')
        studium = studentfil.readline().rstrip('\n')

        if studentnr == oppgitt_studentnr:
            funnet_student = True
            return studentnr, funnet_student

        studentnr = studentfil.readline()
    studentfil.close()


def main():
    avlsutt = True
    while avlsutt:

        hentet_studentnr, status = sjekk_student()

        if status == True:
            skriv_karakterliste(hentet_studentnr)

        ny_utskrift = input('Ønsker du nu utskrift j/n: ')

        if ny_utskrift == 'j':
            avlsutt = True
        else:
            avlsutt = False


main()
