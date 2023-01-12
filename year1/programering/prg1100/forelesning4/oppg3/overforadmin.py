import sys

try:
    studentfil = open('studenter.txt', 'r', encoding='utf-8')

except IOError:
    print('fant ikke fil')

studenter = []

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


def utskrift_av_tabell():
    for r in range(listelengde):
        print('studentnr:', studenter[r][0], 'Fornavn:', studenter[r][1], 'Etternavn:', studenter[r][2], 'E-post:',
              studenter[r][3], 'Fødselsdato:', studenter[r][4], 'Kjønn:', studenter[r][5], 'Studium:', studenter[r][6])


def utskrift_av_studenter():
    for r in range(listelengde):
        print('Fornavn:', studenter[r][1], 'Etternavn:',
              studenter[r][2], 'Fødselsdato:', studenter[r][4])


def utskrift_av_kvinnner():
    for r in range(listelengde):
        if studenter[r][5] == 'kvinne':
            print('Fornavn:', studenter[r][1], 'Etternavn:',
                  studenter[r][2], 'E-post:', studenter[r][3])


def utskrift_av_IT_studenter():
    for r in range(listelengde):
        if studenter[r][6] == 'bachlor IT og IS':
            print('studentnr:', studenter[r][0], 'Fornavn:', studenter[r]
                  [1], 'Etternavn:', studenter[r][2], 'Kjønn:', studenter[r][5])


def main():
    fortsett = 'j'
    while fortsett == 'j':
        print('Meny')
        print('Valg.1 Skriv ut hele lista')
        print('valg.2 Skrive ut fornavn,etternavn og fødselsdato for alle studenter')
        print('Valg.3 utskrift av fornavn,etternavn og e-post for alle kvinner')
        print('Valg.4 utskrift av alle bachlor IT og IS studenter')
        print('Valg.5 Avslutt')
        valg = input('Hva ønsker du å ha utskrift av: ')

        if valg == '1':
            utskrift_av_tabell()

        if valg == '2':
            utskrift_av_studenter()

        if valg == '3':
            utskrift_av_kvinnner()

        if valg == '4':
            utskrift_av_IT_studenter()

        if valg == '5':
            fortsett = 'n'


main()
