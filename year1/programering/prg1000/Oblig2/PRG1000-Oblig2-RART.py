import os


def studentregistrering():
    ny_student = 'j'
    while ny_student == 'j':
        funnet = False
        sok = input('Oppgi et studentnr: ')
        studentfil = open('student.txt', 'r')
        studentnr = studentfil.readline()
        while studentnr != '':
            studentnr = studentnr.rstrip('\n')
            fornavn = studentfil.readline().rstrip('\n')
            etternavn = studentfil.readline().rstrip('\n')
            studium = studentfil.readline().rstrip('\n')

            if studentnr == sok:
                print('studenten er allerede registrert')
                funnet = True
            studentnr = studentfil.readline()
        if not funnet:
            studentfil.close()
            studentfil = open('student.txt', 'a')
            fornavn = input('Oppgi fornavn: ')
            etternavn = input('Oppgi etternavn: ')
            studium = input('Oppgi studium: ')
            studentfil.write(sok+'\n'+fornavn+'\n' +
                             etternavn+'\n' + studium+'\n')
            studentfil.close()
        ny_student = input('Ønsker du å legge inn en ny student (j/n): ')


def studentsletting():
    slett_student = 'j'
    while slett_student == 'j':
        funnet = False
        sok = input('Oppgi studentnr på studenten som skal slettes: ')
        eksamensfil = open('eksamensresultat.txt', 'r')

        emnekode = eksamensfil.readline()
        while emnekode != '':
            emnekode = emnekode.rstrip('\n')
            studentnr = eksamensfil.readline().rstrip('\n')
            karakter = eksamensfil.readline().rstrip('\n')

            if studentnr == sok:
                funnet = True
            emnekode = eksamensfil.readline()
        eksamensfil.close()
        if not funnet:
            funnet1 = False
            studentfil = open('student.txt', 'r')
            tempfil = open('temp.txt', 'w')

            studentnr = studentfil.readline()
            while studentnr != '':
                studentnr = studentnr.rstrip('\n')
                fornavn = studentfil.readline().rstrip('\n')
                etternavn = studentfil.readline().rstrip('\n')
                studium = studentfil.readline().rstrip('\n')

                if studentnr != sok:
                    tempfil.write(studentnr+'\n')
                    tempfil.write(fornavn+'\n')
                    tempfil.write(etternavn+'\n')
                    tempfil.write(studium+'\n')
                else:
                    funnet1 = True
                studentnr = studentfil.readline()
            studentfil.close()
            tempfil.close()
            os.remove('student.txt')
            os.rename('temp.txt', 'student.txt')
            if funnet1:
                print('Studenten er slettet')
            else:
                print('Studenten finnes ikke')
        else:
            print('Studenten kan ikke slettes')
        slett_student = input('Ønsker du å slette en ny student? (j/n): ')


def karakterutskrift():
    ny_utskrift = 'j'
    while ny_utskrift == 'j':

        sok = input('Oppgi studentnr på studenten du skal ha utskrift på: ')
        studentfil = open('student.txt', 'r')
        studentnr = studentfil.readline()

        while studentnr != '':
            studentnr = studentnr.rstrip('\n')
            fornavn = studentfil.readline().rstrip('\n')
            etternavn = studentfil.readline().rstrip('\n')
            studium = studentfil.readline().rstrip('\n')

            if studentnr == sok:
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

            if studentnr == sok:
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
        ny_utskrift = input('Ønsker du å srkive ut ny karakterliste (j/n)? ')


def main():
    avlsutt = True
    while avlsutt:
        print('Meny')
        print()
        print('Valg 1- Studentregistrering')
        print('Valg 2- Sletting av student')
        print('Valg 3- Karakterutskrift')
        print()
        print('Valg 4- Avslutt programmet')
        print()
        valg = input('Hva ønsker du å gjøre? ')
        if valg == '1':
            studentregistrering()
        else:
            if valg == '2':
                studentsletting()
            else:
                if valg == '3':
                    karakterutskrift()
                else:
                    avlsutt = False
                    print('Program avsluttet')


main()
