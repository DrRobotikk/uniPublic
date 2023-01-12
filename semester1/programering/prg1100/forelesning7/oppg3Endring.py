import mysql.connector
from tkinter import*

mindatabase = mysql.connector.connect(
    host='localhost', port=3306, user='Lagersjefen2022', passwd='lagerpw', db='heltnydatabase')


def hentVare():
    henterMarkor = mindatabase.cursor()

    henterMarkor.execute("SELECT * FROM Vare")

    liste = []

    for i in henterMarkor:
        liste += [i]
    print(liste)

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


def endrerVare():
    endreMarkor = mindatabase.cursor()

    endreMarkor.execute("SELECT VNr FROM Vare")

    vareliste = []

    for row in endreMarkor:
        vareliste += [[row]]

    funnet = False
    gjennomgang = 0

    while (funnet == False) and (gjennomgang <= len(vareliste)):

        if vnr.get() in vareliste[gjennomgang][0]:

            endreVare = ("update Vare SET Antall=%s WHERE VNr=%s")
            endreData = (vantall.get(), vnr.get())

            endreMarkor.execute(endreVare, endreData)
            mindatabase.commit()

            funnet = True
        else:
            gjennomgang += 1

    endreMarkor.close()


window = Tk()
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
entVhylle = Entry(window, width=4, textvariable=vhylle, state="readonly")
entVhylle.grid(row=5, column=1, padx=5, pady=5, sticky=W)


btnLagre = Button(window, text='Lagre', command=endrerVare)
btnLagre.grid(row=6, column=2, padx=5, pady=5, sticky=W)

btnAvslutt = Button(window, text='Avslutt', command=window.destroy)
btnAvslutt.grid(row=6, column=3, padx=5, pady=5, sticky=W)

btnHentVare = Button(window, text="Hent vare", command=hentVare)
btnHentVare.grid(row=0, column=2, padx=5, pady=5, sticky=E)

window.mainloop()

mindatabase.close()
