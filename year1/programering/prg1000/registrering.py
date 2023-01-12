def studentregistrering():
    nystudent = 'j'
    while nystudent == 'j':
        sok = input('Oppgi et studentnr: ')
        studentfil = open('student.txt', 'r')
        studentnr = studentfil.readline()
        funnet = False
        while studentnr != '':
            studentnr = studentnr.rstrip('\n')
            fornavn = studentfil.readline().rstrip('\n')
            etternavn = studentfil.readline().rstrip('\n')
            studium = studentfil.readline().rstrip('\n')

            if studentnr == sok:
                print('studenten er allerede registrert')
                funnet = True
        studentfil.close()
        if not funnet:
            studentfil = open('student.txt', 'a')
            fornavn = input('Oppgi fornavn: ')
            etternavn = input('Oppgi etternavn: ')
            studium = input('Oppgi studium: ')
            studentfil.write(sok+'\n'+fornavn+'\n' +
                             etternavn+'\n' + studium+'\n')
            studentfil.close()
        nystudent = input('Ønsker du å legge inn en ny student (j/n): ')


studentregistrering()
