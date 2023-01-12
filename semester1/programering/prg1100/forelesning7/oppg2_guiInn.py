import mysql.connector
from tkinter import*


def setterInnVare():

    settinnmarkor = mindatabase.cursor()

    settinnvare = ("INSERT INTO Vare"
                   "(VNr,Betegnelse,Pris,KatNr,Antall,Hylle)"
                   "VALUES(%s,%s,%s,%s,%s,%s)")

    datanyVare = (vnr.get(), vnavn.get(), vpris.get(),
                  vkatnr.get(), vantall.get(), vhylle.get())

    settinnmarkor.execute(settinnvare, datanyVare)
    mindatabase.commit()

    settinnmarkor.close()


mindatabase = mysql.connector.connect(
    host='localhost', port=3306, user='Lagersjefen2022', passwd='lagerpw', db='heltnydatabase')


window = Tk()
window.title('Nye varer')

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
entVnavn = Entry(window, width=20, textvariable=vnavn)
entVnavn.grid(row=1, column=1, padx=5, pady=5, sticky=W)

vpris = StringVar()
entVpris = Entry(window, width=5, textvariable=vpris)
entVpris.grid(row=2, column=1, padx=5, pady=5, sticky=W)

vkatnr = StringVar()
entVkatnr = Entry(window, width=4, textvariable=vkatnr)
entVkatnr.grid(row=3, column=1, padx=5, pady=5, sticky=W)

vantall = StringVar()
entVantall = Entry(window, width=4, textvariable=vantall)
entVantall.grid(row=4, column=1, padx=5, pady=5, sticky=W)

vhylle = StringVar()
entVhylle = Entry(window, width=4, textvariable=vhylle)
entVhylle.grid(row=5, column=1, padx=5, pady=5, sticky=W)


btnLagre = Button(window, text='Lagre', command=setterInnVare)
btnLagre.grid(row=6, column=2, padx=5, pady=5, sticky=W)

btnAvslutt = Button(window, text='Avslutt', command=window.destroy)
btnAvslutt.grid(row=6, column=3, padx=5, pady=5, sticky=W)

window.mainloop()


mindatabase.close()
