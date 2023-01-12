def innlesning_dictionary():
    studenter = {}
    studentfil = open('studenter.txt', 'r', encoding='utf-8')

    studentnr = studentfil.readline()

    while studentnr != '':
        studentnr = studentnr.rstrip('\n')
        fornavn = studentfil.readline().rstrip('\n')
        etternavn = studentfil.readline().rstrip('\n')
        epost = studentfil.readline().rstrip('\n')
        fodselsdato = studentfil.readline().rstrip('\n')
        kjonn = studentfil.readline().rstrip('\n')
        studium = studentfil.readline().rstrip('\n')

        studenter[studentnr] = [fornavn, etternavn,
                                epost, fodselsdato, kjonn, studium]

        studentnr = studentfil.readline()
    studentfil.close()

    return studenter


def innlesning_dictionary2():
    studenter = {}

    studentfil = open('studenter.txt', 'r', encoding='utf-8')

    studentnr = studentfil.readline()

    while studentnr != '':
        studentnr = studentnr.rstrip('\n')
        fornavn = studentfil.readline().rstrip('\n')
        etternavn = studentfil.readline().rstrip('\n')
        epost = studentfil.readline().rstrip('\n')
        fodselsdato = studentfil.readline().rstrip('\n')
        kjonn = studentfil.readline().rstrip('\n')
        studium = studentfil.readline().rstrip('\n')

        studenter[studentnr] = {'fornavn': fornavn, 'etternavn': etternavn,
                                'epost': epost, 'fodselsdato': fodselsdato, 'kjonn': kjonn, 'studium': studium}
        studentnr = studentfil.readline()
    studentfil.close()

    return studenter


def utskrift_av_antall_kvinner2():
    studentdic = innlesning_dictionary2()

    antall_kvinner = 0

    for key in studentdic:
        if studentdic[key]['kjonn'].upper() == 'KVINNE':
            antall_kvinner += 1

    print('antallet kvinner er ', antall_kvinner)


def antall_paa_studier2():
    studentdic = innlesning_dictionary2()

    antall_it = 0
    antall_ok = 0

    for key in studentdic:
        if studentdic[key]['studium'].upper() == 'BACHLOR IT OG IS':
            antall_it += 1
        if studentdic[key]['studium'].upper() == 'BACHLOR ØKADM':
            antall_ok += 1
    print('Antall på it er ', antall_it)
    print('antall på idiotsutdie  er ', antall_ok)


def utskrift_av_antall_kvinner():
    studentdic = innlesning_dictionary()

    antall_kvinner = 0
    for key in studentdic:
        if studentdic[key][4] == 'kvinne':
            antall_kvinner += 1

    print('Antallet kvinner er ', antall_kvinner)


def utskrfit_av_antall_paa_studie():
    studentdic = innlesning_dictionary()

    antall_it = 0
    antall_okad = 0

    for key in studentdic:
        if studentdic[key][5].upper() == 'BACHLOR IT OG IS':
            antall_it += 1
        if studentdic[key][5].upper() == 'BACHLOR ØKADM':
            antall_okad += 1

    print('antall It studenter er ', antall_it)
    print()
    print('Antallet studenter på økad er ', antall_okad)


def main():
    ny_utskrift = 'j'
    while ny_utskrift == 'j':
        print('meny')
        print('Valg.1 utskrift av antall kvinner')
        print('Valg.2 utskrift av antall på vert studium')
        print('Valg.3 utskrift av antall kvinner på annen måte')
        print('Valg.4 utskrift av antall studenter på studie i annen versjon')
        print('Valg.5 Avslutt')

        valg = input('Hva ønsker du å gjøre: ')

        if valg == '1':
            utskrift_av_antall_kvinner()

        if valg == '2':
            utskrfit_av_antall_paa_studie()

        if valg == '3':
            utskrift_av_antall_kvinner2()

        if valg == '4':
            antall_paa_studier2()

        if valg == '5':
            ny_utskrift = 'n'


try:
    main()

except IOError:
    print('Fant ikke filen')
