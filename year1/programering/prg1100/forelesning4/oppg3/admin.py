import sys
fortsett = 'j'

while fortsett == 'j':
    try:
        studenter = []
        studentfil = open('studenter.txt', 'r')

        studentnr = studentfil.readline()

        while studentnr != '':
            studentnr = studentnr.rstrip('\n')
            fornavn = studentfil.readline().rstrip('\n')
            etternavn = studentfil.readline().rstrip('\n')
            e_post = studentfil.readline().rstrip('\n')
            fodselsdato = studentfil.readline().rstrip('\n')
            kjonn = studentfil.readline().rstrip('\n')
            studium = studentfil.readline().rstrip('\n')

            studenter += [[studentnr, fornavn, etternavn,
                           e_post, fodselsdato, kjonn, studium]]

            studentnr = studentfil.readline()

        studentfil.close()

        listelengde = len(studenter)
        print('Meny')
        print('Valg.1 Skriv ut hele lista')
        print('valg.2 Skrive ut fornavn,etternavn og fødselsdato for alle studenter')
        print('Valg.3 utskrift av fornavn,etternavn og e-post for alle kvinner')
        print('Valg.4 utskrift av alle bachlor IT og IS studenter')
        valg = input('Hva ønsker du å ha utskrift av: ')

        if valg == '1':
            for r in range(listelengde):
                print('studentnr:', studenter[r][0], 'Fornavn:', studenter[r][1], 'Etternavn:', studenter[r][2], 'E-post:',
                      studenter[r][3], 'Fødselsdato:', studenter[r][4], 'Kjønn:', studenter[r][5], 'Studium:', studenter[r][6])
        if valg == '2':
            for r in range(listelengde):
                print('Fornavn:', studenter[r][1], 'Etternavn:',
                      studenter[r][2], 'Fødselsdato:', studenter[r][4])
        if valg == '3':
            for r in range(listelengde):
                if studenter[r][5] == 'kvinne':
                    print('Fornavn:', studenter[r][1], 'Etternavn:',
                          studenter[r][2], 'E-post:', studenter[r][3])
        if valg == '4':
            for r in range(listelengde):
                if studenter[r][6] == 'bachlor IT og IS':
                    print('studentnr:', studenter[r][0], 'Fornavn:', studenter[r]
                          [1], 'Etternavn:', studenter[r][2], 'Kjønn:', studenter[r][5])
    except IOError:
        print('Fant ikke filen')

    fortsett = input('Ønsker du en annen utskrift j/n: ')
