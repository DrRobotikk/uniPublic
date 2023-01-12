# Lager funksjonen for å lese fra fil til tabell
def innlesning_av_fil():
    varefil = open('Varer.txt', 'r', encoding='UTF-8')

    vare = []
    varenr = varefil.readline()

    while varenr != '':
        varenr = varenr.rstrip('\n')
        betegnelse = varefil.readline().rstrip('\n')
        pris = varefil.readline().rstrip('\n')
        kategori = varefil.readline().rstrip('\n')
        hylle = varefil.readline().rstrip('\n')

        vare += [[varenr, betegnelse, pris, kategori, hylle]]

        varenr = varefil.readline()
    varefil.close()

    listelengde = len(vare)

    return vare, listelengde


# Lager funksjonen for å printe ut varer og hylleplass
def skrive_ut_varer_og_hylleplass(skrive_ut_varer_og_hylleplassVareliste, skrive_ut_varer_og_hylleplassListelengde):
    for r in range(skrive_ut_varer_og_hylleplassListelengde):
        print('betegnelse:', skrive_ut_varer_og_hylleplassVareliste[r]
              [1], 'hylle:', skrive_ut_varer_og_hylleplassVareliste[r][4])


# Lager funksjon for å skrive ut varer uten hylleplassering
def Skrive_ut_varer_uten_hylle(skrive_ut_varer_uten_hylleVareliste, skrive_ut_varer_uten_hylleListelengde):
    for r in range(skrive_ut_varer_uten_hylleListelengde):
        if skrive_ut_varer_uten_hylleVareliste[r][4] == 'NULL':
            print(skrive_ut_varer_uten_hylleVareliste[r][0], skrive_ut_varer_uten_hylleVareliste[r][1],
                  skrive_ut_varer_uten_hylleVareliste[r][2], skrive_ut_varer_uten_hylleVareliste[r][3], skrive_ut_varer_uten_hylleVareliste[r][4])


# Lager funksjonen for å skirve ut alle varer på gitt forbokstav
def skrive_ut_brukeroppgitt_bokstav(skrive_ut_brukeroppgitt_bokstavVareliste, skrive_ut_brukeroppgitt_bokstavListelengde):
    oppgitt_bokstav = input('Oppgi en bokstav: ')

    for r in range(skrive_ut_brukeroppgitt_bokstavListelengde):
        if skrive_ut_brukeroppgitt_bokstavVareliste[r][1][0:1].upper() == oppgitt_bokstav.upper():
            print(skrive_ut_brukeroppgitt_bokstavVareliste[r][0], skrive_ut_brukeroppgitt_bokstavVareliste[r][1],
                  skrive_ut_brukeroppgitt_bokstavVareliste[r][2], skrive_ut_brukeroppgitt_bokstavVareliste[r][3], skrive_ut_brukeroppgitt_bokstavVareliste[r][4])


# Lager funksjonen for å skrive ut etter oppgitt kategori og teller antall
def brukeroppgitt_kategori_og_antall(brukeroppgitt_kategori_og_antallVareliste, brukeroppgitt_kategori_og_antallListelengde):
    antall_varer = 0
    oppgitt_kategori = input('Oppgi en kategori: ')

    for r in range(brukeroppgitt_kategori_og_antallListelengde):
        if brukeroppgitt_kategori_og_antallVareliste[r][3].upper() == oppgitt_kategori.upper():
            antall_varer += 1
            print(brukeroppgitt_kategori_og_antallVareliste[r][0], brukeroppgitt_kategori_og_antallVareliste[r][1],
                  brukeroppgitt_kategori_og_antallVareliste[r][2],  brukeroppgitt_kategori_og_antallVareliste[r][4])
    print(antall_varer)

# Lager funksjonen for å printe ut varer innenfor et gitt prisintervall


def skrive_ut_prisintervall(Skrive_ut_prisintervallVareliste, skrive_ut_prisintervallListelengde):
    for r in range(skrive_ut_prisintervallListelengde):
        if float(Skrive_ut_prisintervallVareliste[r][2]) >= 100 and float(Skrive_ut_prisintervallVareliste[r][2]) <= 200:
            print(Skrive_ut_prisintervallVareliste[r][0], Skrive_ut_prisintervallVareliste[r][1],
                  Skrive_ut_prisintervallVareliste[r][3], Skrive_ut_prisintervallVareliste[r][4])

# Lager funksjonen for å sortere tabellen og legge den til en ny fil


def sortering_av_liste(sortering_av_listeVareliste, sortering_av_listeListelengde):

    bytte = True
    stoppmerke = 1

    while bytte:
        bytte = False
        for r in range(sortering_av_listeListelengde-stoppmerke):
            if sortering_av_listeVareliste[r][1] > sortering_av_listeVareliste[r+1][1]:
                bytte = True
                byttevariabel = sortering_av_listeVareliste[r]
                sortering_av_listeVareliste[r] = sortering_av_listeVareliste[r+1]
                sortering_av_listeVareliste[r+1] = byttevariabel

        stoppmerke += 1
    sortert_varer_fil = open('SortertVare.txt', 'w', encoding='UTF-8')

    for r in range(sortering_av_listeListelengde):
        sortert_varer_fil.write(
            sortering_av_listeVareliste[r][0]+'\n' + sortering_av_listeVareliste[r][1]+'\n' + sortering_av_listeVareliste[r][2]+'\n' + sortering_av_listeVareliste[r][3]+'\n')
    sortert_varer_fil.close()

# Lager main med meny struktur


def main():
    fortsett = True
    while fortsett:
        # Lager en while-løkke for å sørge for at en bare leser inn når det er nødvendig
        innlesing = True
        while innlesing:
            hentet_liste, hentet_listelengde = innlesning_av_fil()
            innlesing = False
        print('Meny')
        print()
        print('Valg.1, skriv ut alle varer og hylleplass')
        print('Valg.2, skriv ut alle varer som ikke er hylleplasert')
        print(
            'Valg.3, oppgi en bokstav og skriv ut alle varer som starter på denne bokstaven')
        print('valg.4, Skriv ut alle varer innenfor en oppgit kategori og antallet')
        print('Valg.5, alle varer mellom 100kr og 200kr')
        print('Valg.6, Sorter lista og legg den sorterte lista på ny fil')
        print('valg.7, Avslutt programmet')
        valg = input('Oppgi et valg: ')

        if valg == '1':
            print()
            skrive_ut_varer_og_hylleplass(hentet_liste, hentet_listelengde)
            print()

        if valg == '2':
            print()
            Skrive_ut_varer_uten_hylle(hentet_liste, hentet_listelengde)
            print()

        if valg == '3':
            print()
            skrive_ut_brukeroppgitt_bokstav(hentet_liste, hentet_listelengde)
            print()

        if valg == '4':
            print()
            brukeroppgitt_kategori_og_antall(hentet_liste, hentet_listelengde)
            print()

        if valg == '5':
            print()
            skrive_ut_prisintervall(hentet_liste, hentet_listelengde)
            print()

        if valg == '6':
            print()
            sortering_av_liste(hentet_liste, hentet_listelengde)
            print()
            innlesing = True

        if valg == '7':
            fortsett = False
            print('Programmet er avsluttet')


# Legger main i try blokka og ber brukeren kjøre på nytt hvis IOError dukker opp
try:
    main()

except IOError:
    print('fant ikke filen, se om filen ligger riktig og kjør på nytt')
