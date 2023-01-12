import os


def sjekk_student():
    funnet_student = False
    oppgitt_studentnr = input('Oppgi et studentnr: ')

    studentfil = open('student.txt', 'r')

    studnr = studentfil.readline()

    while studnr != '':
        studnr = studnr.rstrip('\n')
        fnavn = studentfil.readline().rstrip('\n')
        enavn = studentfil.readline().rstrip('\n')
        studium = studentfil.readline().rstrip('\n')

        if studnr == oppgitt_studentnr:
            funnet_student = True

        studnr = studentfil.readline()
    studentfil.close()
    return oppgitt_studentnr, funnet_student


def sjekke_resultat(sjekke_resultatStudentnr):
    funnet_resultat = False
    resultatfil = open('eksamensresultat.txt', 'r')

    ekode = resultatfil.readline()

    while ekode != '':
        ekode = ekode.rstrip('\n')
        studnr = resultatfil.readline().rstrip('\n')
        karakter = resultatfil.readline().rstrip('\n')

        if studnr == sjekke_resultatStudentnr:
            funnet_resultat = True
        ekode = resultatfil.readline()
    resultatfil.close()
    return funnet_resultat


def henter_navn(henter_navnStudentnr):
    funnet_student = False

    studentfil = open('student.txt', 'r')

    studnr = studentfil.readline()

    while studnr != '':
        studnr = studnr.rstrip('\n')
        fnavn = studentfil.readline().rstrip('\n')
        enavn = studentfil.readline().rstrip('\n')
        studium = studentfil.readline().rstrip('\n')

        if studnr == henter_navnStudentnr:
            funnet_student = True
            return fnavn, enavn, studium
        studnr = studentfil.readline()
    studentfil.close()


def henter_karakterer(henter_karaktererStudentnr):
    funnet_resultat = False

    eksamensfil = open('eksamensresultat.txt', 'r')

    ekode = eksamensfil.readline()

    while ekode != '':
        ekode = ekode.rstrip('\n')
        studnr = eksamensfil.readline().rstrip('\n')
        karakter = eksamensfil.readline().rstrip('\n')

        if studnr == henter_karaktererStudentnr:
            funnet_resultat = True
            return karakter, ekode
        ekode = eksamensfil.readline()
    eksamensfil.close()


def registrere_student():
    ny_registrering = 'j'
    while ny_registrering == 'j':
        studentnummer, status = sjekk_student()

        if status == False:
            oppgitt_fnavn = input('Oppgi fornavnet: ')
            oppgitt_enavn = input('Oppgi etternavnet: ')
            oppgitt_studium = input('Oppgi studium: ')

            studfil = open('student.txt', 'a')

            studfil.write(studentnummer+'\n')
            studfil.write(oppgitt_fnavn+'\n')
            studfil.write(oppgitt_enavn+'\n')
            studfil.write(oppgitt_studium+'\n')
            studfil.close()
            print()
            print('Studenten er registrert')
            print()

        if status == True:
            print('Studenten er allerede registrert')
        ny_registrering = input('Ønsker du å registrere enda en student j/n: ')


def slette_student():
    ny_slett = 'j'
    while ny_slett == 'j':
        studentnr, status = sjekk_student()

        if status == True:
            status_resultat = sjekke_resultat(studentnr)

        if status_resultat == True:
            print('Student kan ikke slettes')

        if status == True and status_resultat == False:
            sikker = input(
                'Er du sikker på at du vil slette denne studenten ' + studentnr + ' j/n ')

            if sikker == 'j':
                studentfil = open('student.txt', 'r')
                tempfil = open('temp.txt', 'w')

                studnr = studentfil.readline()

                while studnr != '':
                    studnr = studnr.rstrip('\n')
                    fnavn = studentfil.readline().rstrip('\n')
                    enavn = studentfil.readline().rstrip('\n')
                    studium = studentfil.readline().rstrip('\n')

                    if studnr != studentnr:
                        tempfil.write(studnr+'\n')
                        tempfil.write(fnavn+'\n')
                        tempfil.write(enavn+'\n')
                        tempfil.write(studium+'\n')

                    studnr = studentfil.readline()
                studentfil.close()
                tempfil.close()

                os.remove('student.txt')
                os.rename('temp.txt', 'student.txt')
                print('studenten er slettet')
        ny_slett = input('Ønsker du å slette enda en student j/n: ')


def skriv_karakterliste():
    ny_utskrift = 'j'
    while ny_utskrift == 'j':
        Studentnummer, status = sjekk_student()
        fornavn, etternavn, studium = henter_navn(Studentnummer)
        print(fornavn, etternavn, studium)
        print()

        karakter, emnekode = henter_karakterer(Studentnummer)
        print(karakter, emnekode)

        ny_utskrift = input('Ønkser du enda en utskrift j/n: ')


def main():
    avslutt = 'n'
    while avslutt == 'n':
        print('Meny')
        print()
        print('Valg 1, studentregistrering')
        print('Valg 2, sletting av student')
        print('Valg 3, Karakterutskrift for student')
        print('Valg 4, Avslutt')
        print()
        valg = input('Hva ønsker du å gjøre? 1,2,3 eller 4: ')

        if valg == '1':
            registrere_student()
        if valg == '2':
            slette_student()
        if valg == '3':
            skriv_karakterliste()
        if valg == '4':
            avslutt = 'j'


main()
