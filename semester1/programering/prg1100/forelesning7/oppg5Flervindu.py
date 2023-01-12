import mysql.connector
from tkinter import*
from tkinter import messagebox

# Legg til med sjekking i databasen om varen VNr finnes
# Gjøre andre forbedringer

mindatabase = mysql.connector.connect(
    host='localhost', port=3306, user='Lagersjefen2022', passwd='lagerpw', db='heltnydatabase')


def sjekkVare(sjekk_vareVNr):
    dataListe = []
    sjekkMarkor = mindatabase.cursor()

    sjekkMarkor.execute("SELECT * FROM Vare")

    for row in sjekkMarkor:
        dataListe += [row]

    funnet = False
    rad = 0

    while (funnet == False) and (rad <= len(dataListe)-1):
        if sjekk_vareVNr == dataListe[rad][0]:
            funnet = True
        rad += 1

    return funnet
    sjekkMarkor.close()


def henterWindow5():
    def slettVare():

        status = sjekkVare(slettvnr.get())

        if status == True:
            slettVareMarkor = mindatabase.cursor()

            slettVaresql = ("DELETE FROM Vare WHERE VNr=%s")

            slettVareMarkor.execute(slettVaresql, (slettvnr.get(),))
            mindatabase.commit()
            messagebox.showinfo('Vellykket', 'varen er slettet')

        slettVareMarkor.close()

    window5 = Toplevel()
    window5.title('Slett vare')

    lblVarenr = Label(window5, text='Legg inn VNr')
    lblVarenr.grid(row=0, column=0, padx=5, pady=5, sticky=E)

    slettvnr = StringVar()
    entVarenr = Entry(window5, width=5, textvariable=slettvnr)
    entVarenr.grid(row=0, column=1, padx=5, pady=5, sticky=W)

    btnSlett = Button(window5, text='Slett vare', command=slettVare)
    btnSlett.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky=EW)

    btnTilbake = Button(window5, text='Tilbake', command=window5.destroy)
    btnTilbake.grid(row=2, column=1, padx=5, pady=5, sticky=E)


def henterWindow4():
    def hentVare():

        henterMarkor = mindatabase.cursor()

        henterMarkor.execute("SELECT * FROM Vare")

        liste = []

        for i in henterMarkor:
            liste += [i]

        fant = False
        radnr = 0

        while (fant == False) and (radnr <= len(liste)-1):
            if vnr.get() == liste[radnr][0]:
                vnavn.set(liste[radnr][1])
                vpris.set(liste[radnr][2])
                vkatnr.set(liste[radnr][3])
                vantall.set(liste[radnr][4])
                vhylle.set(liste[radnr][5])
                fant = True
            else:
                radnr += 1
        henterMarkor.close()

    def endreVare():

        status = sjekkVare(vnr.get())

        if status == True:
            endreMarkor = mindatabase.cursor()
            endreVare = ("update Vare SET Antall=%s WHERE VNr=%s")
            endreData = (vantall.get(), vnr.get())

            endreMarkor.execute(endreVare, endreData)
            mindatabase.commit()
            messagebox.showinfo('funket', 'Endring er gjort')

        endreMarkor.close()

    window = Toplevel()
    window.title('endring av vare')

    lblVarenr = Label(window, text='Oppgi varenr: ')
    lblVarenr.grid(row=0, column=0, padx=5, pady=5, sticky=E)

    lblVarenavn = Label(window, text='Oppgi varenavn: ')
    lblVarenavn.grid(row=1, column=0, padx=5, pady=5, sticky=E)

    lblPris = Label(window, text='Oppgi pris: ')
    lblPris.grid(row=2, column=0, padx=5, pady=5, sticky=E)

    lblKatnr = Label(window, text='Oppgi kategorinr: ')
    lblKatnr.grid(row=3, column=0, padx=5, pady=5, sticky=E)

    lblAntall = Label(window, text='Oppgi antall: ')
    lblAntall.grid(row=4, column=0, padx=5, pady=5, sticky=E)

    lblHylle = Label(window, text='Oppgi hylleplassering: ')
    lblHylle.grid(row=5, column=0, padx=5, pady=5, sticky=E)

    vnr = StringVar()
    entVnr = Entry(window, width=6, textvariable=vnr)
    entVnr.grid(row=0, column=1, padx=5, pady=5, sticky=W)

    vnavn = StringVar()
    entVnavn = Entry(window, width=20, textvariable=vnavn, state="readonly")
    entVnavn.grid(row=1, column=1, padx=5, pady=5, sticky=W)

    vpris = StringVar()
    entVpris = Entry(window, width=5, textvariable=vpris, state="readonly")
    entVpris.grid(row=2, column=1, padx=5, pady=5, sticky=W)

    vkatnr = StringVar()
    entVkatnr = Entry(window, width=4, textvariable=vkatnr, state="readonly")
    entVkatnr.grid(row=3, column=1, padx=5, pady=5, sticky=W)

    vantall = StringVar()
    entVantall = Entry(window, width=4, textvariable=vantall)
    entVantall.grid(row=4, column=1, padx=5, pady=5, sticky=W)

    vhylle = StringVar()
    entVhylle = Entry(window, width=4, textvariable=vhylle,
                      state="readonly", bg='grey')
    entVhylle.grid(row=5, column=1, padx=5, pady=5, sticky=W)

    btnLagre = Button(window, text='Lagre', command=endreVare)
    btnLagre.grid(row=6, column=2, padx=5, pady=5, sticky=W)

    btnAvslutt = Button(window, text='Tilbake', command=window.destroy)
    btnAvslutt.grid(row=6, column=3, padx=5, pady=5, sticky=W)

    btnHentVare = Button(window, text="Hent vare", command=hentVare)
    btnHentVare.grid(row=0, column=2, padx=5, pady=5, sticky=E)


def henterWindow2():
    def hent_prisoglager(event):
        valgt = lst_varer.get(lst_varer.curselection())

        prisoglager_markor = mindatabase.cursor()
        prisoglager_markor.execute('SELECT Betegnelse,Pris,Antall FROM Vare')

        vareListe = []

        for row in prisoglager_markor:
            vareListe += [row]

        funnet = False
        radnr = 0

        while (funnet == False) and (radnr <= len(vareListe)-1):
            if valgt == vareListe[radnr][0]:
                pris.set(vareListe[radnr][1])
                lager.set(vareListe[radnr][2])
                funnet = True
            else:
                radnr += 1

        prisoglager_markor.close()

    vare_markor = mindatabase.cursor()

    vare_markor.execute('SELECT betegnelse FROM Vare')

    varer = []
    for row in vare_markor:
        varer += [row[0]]

    window2 = Toplevel()
    window2.title('Varer')
    y_scroll = Scrollbar(window2, orient=VERTICAL)
    y_scroll.grid(row=0, column=2, rowspan=10,
                  padx=(0, 100), pady=5, sticky=NS)

    innhold_i_lst_varer = StringVar()
    lst_varer = Listbox(window2, width=50, height=10,
                        listvariable=innhold_i_lst_varer, yscrollcommand=y_scroll.set)
    lst_varer.grid(row=0, column=1, rowspan=10,
                   padx=(100, 0), pady=5, sticky=E)
    innhold_i_lst_varer.set(tuple(varer))
    y_scroll['command'] = lst_varer.yview

    lbl_pris = Label(window2, text='Prsien er:')
    lbl_pris.grid(row=0, column=3, padx=5, pady=5, sticky=E)
    lbl_lager = Label(window2, text='Lagerstatusen er:')
    lbl_lager.grid(row=1, column=3, padx=5, pady=5, sticky=E)

    pris = StringVar()
    ent_pris = Entry(window2, width=10, state='readonly', textvariable=pris)
    ent_pris.grid(row=0, column=4, padx=5, pady=5, sticky=W)
    lager = StringVar()
    ent_lager = Entry(window2, width=10, state='readonly', textvariable=lager)
    ent_lager.grid(row=1, column=4, padx=5, pady=5, sticky=W)

    btnAvslutt = Button(window2, text='Tilbake', command=window2.destroy)
    btnAvslutt.grid(row=2, column=4, padx=5, pady=5, sticky=E)

    lst_varer.bind('<<ListboxSelect>>', hent_prisoglager)

    vare_markor.close()


def henterWindow3():
    def vareInnlagt():
        settinnmarkor = mindatabase.cursor()

        settinnvare = ("INSERT INTO Vare"
                       "(VNr,Betegnelse,Pris,KatNr,Antall,Hylle)"
                       "VALUES(%s,%s,%s,%s,%s,%s)")

        datanyVare = (vnr.get(), vnavn.get(), vpris.get(),
                      vkatnr.get(), vantall.get(), vhylle.get())

        settinnmarkor.execute(settinnvare, datanyVare)
        mindatabase.commit()

        settinnmarkor.close()

    window3 = Toplevel()
    window3.title('Nye varer')

    lblVarenr = Label(window3, text='Oppgi varenr: ')
    lblVarenr.grid(row=0, column=0, padx=5, pady=5, sticky=E)

    lblVarenavn = Label(window3, text='Oppgi varenavn: ')
    lblVarenavn.grid(row=1, column=0, padx=5, pady=5, sticky=E)

    lblPris = Label(window3, text='Oppgi pris: ')
    lblPris.grid(row=2, column=0, padx=5, pady=5, sticky=E)

    lblKatnr = Label(window3, text='Oppgi kategorinr: ')
    lblKatnr.grid(row=3, column=0, padx=5, pady=5, sticky=E)

    lblAntall = Label(window3, text='Oppgi antall: ')
    lblAntall.grid(row=4, column=0, padx=5, pady=5, sticky=E)

    lblHylle = Label(window3, text='Oppgi hylleplassering: ')
    lblHylle.grid(row=5, column=0, padx=5, pady=5, sticky=E)

    vnr = StringVar()
    entVnr = Entry(window3, width=6, textvariable=vnr)
    entVnr.grid(row=0, column=1, padx=5, pady=5, sticky=W)

    vnavn = StringVar()
    entVnavn = Entry(window3, width=20, textvariable=vnavn)
    entVnavn.grid(row=1, column=1, padx=5, pady=5, sticky=W)

    vpris = StringVar()
    entVpris = Entry(window3, width=5, textvariable=vpris)
    entVpris.grid(row=2, column=1, padx=5, pady=5, sticky=W)

    vkatnr = StringVar()
    entVkatnr = Entry(window3, width=4, textvariable=vkatnr)
    entVkatnr.grid(row=3, column=1, padx=5, pady=5, sticky=W)

    vantall = StringVar()
    entVantall = Entry(window3, width=4, textvariable=vantall)
    entVantall.grid(row=4, column=1, padx=5, pady=5, sticky=W)

    vhylle = StringVar()
    entVhylle = Entry(window3, width=4, textvariable=vhylle)
    entVhylle.grid(row=5, column=1, padx=5, pady=5, sticky=W)

    btnLagre = Button(window3, text='Lagre', command=vareInnlagt)
    btnLagre.grid(row=6, column=2, padx=5, pady=5, sticky=W)

    btnAvslutt = Button(window3, text='Tilbake', command=window3.destroy)
    btnAvslutt.grid(row=6, column=3, padx=5, pady=5, sticky=W)


def main():
    window = Tk()
    window.title('Hovedmeny')

    btnSeData = Button(window, text='Se databasens innhold',
                       command=henterWindow2)
    btnSeData.grid(row=0, column=0, padx=5, pady=5, sticky=W)

    btnNyVare = Button(window, text='Legge til ny vare', command=henterWindow3)
    btnNyVare.grid(row=0, column=1, padx=5, pady=5, sticky=W)

    btnEndre = Button(window, text='Endre vare', command=henterWindow4)
    btnEndre.grid(row=0, column=2, padx=5, pady=5, sticky=W)

    btnSlett = Button(window, text='Slett en vare', command=henterWindow5)
    btnSlett.grid(row=0, column=3, padx=5, pady=5, sticky=W)

    btnAvslutt = Button(window, text='Avslutt', command=window.destroy)
    btnAvslutt.grid(row=1, column=3, padx=5, pady=5, sticky=E)

    window.mainloop()


main()
mindatabase.close()
