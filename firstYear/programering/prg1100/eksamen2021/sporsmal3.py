import mysql.connector
from tkinter import *

mindatabase = mysql.connector.connect(host='localhost', port=3306,
                                      user='Dekksjef', passwd='Eksamen2021', db='Dekkhotell')


def sjekk_kunde():
    sjekk_markor = mindatabase.cursor()
    kundeliste = []
    mobil = nr.get()
    funnet = False

    sjekk_markor.execute('''
                        SELECT Mobilnr
                        FROM Kunde
                        ''')
    for row in sjekk_markor:
        kundeliste += [[row[0]]]
    sjekk_markor.close()

    funnet = False
    rad = 0

    while (funnet == False) and (rad <= len(kundeliste)-1):
        if mobil == kundeliste[rad][0]:
            funnet = True

        rad += 1

        if funnet == True:
            lbl_svar.config(text='Finnes')
        if funnet == False:
            lbl_svar.config(text='Finnes ikke')

def lagre_info():
    mobil=nr.get()
    fnavn=fornavn.get()
    enavn=etter.get()
    eposten=epost.get()
    rnr=regnr.get()
    hyllenr=hylle.get()

    kundemarkor=mindatabase.cursor()

    kundedata=(mobil,fnavn,enavn,eposten)

    kundesql=('''INSERT INTO Kunde(Mobilnr,Fornavn,Etternavn,Epost) VALUES (%s,%s,%s,%s) ''')

    kundemarkor.execute(kundesql,kundedata)
    mindatabase.commit()

    kundemarkor.close()

    settmarkor=mindatabase.cursor()

    settdata=(mobil,rnr)

    settsql=('''INSERT INTO Dekksett(Mobilnr,Regnr) VALUES (%s,%s) ''')

    settmarkor.execute(settsql,settdata)
    mindatabase.commit()

    settmarkor.close()

    oppbevaingMarkor=mindatabase.cursor()

    oppbevaringdata=(mobil,rnr,hyllenr)

    oppbevaringsql=('''INSERT INTO Oppbevaring(Mobilnr,Regnr,Innlevert,Utlevert,Hylle,Pris) VALUES (%s,%s,CURRENT_TIMESTAMP,NULL,%s,NULL) ''')

    oppbevaingMarkor.execute(oppbevaringsql,oppbevaringdata)
    mindatabase.commit()
    oppbevaingMarkor.close()




vindu = Tk()
vindu.title('Oppbevaringsoversikt')

lbl_nr = Label(vindu, text='Mobilnr')
lbl_nr.grid(row=0, column=0, padx=10, pady=10, sticky=W)

lbl_fornavn = Label(vindu, text='Fornavn')
lbl_fornavn.grid(row=1, column=0, padx=10, pady=10, sticky=W)

lbl_etter = Label(vindu, text='Etternavn')
lbl_etter.grid(row=2, column=0, padx=10, pady=10, sticky=W)

lbl_epost = Label(vindu, text='Epost')
lbl_epost.grid(row=3, column=0, padx=10, pady=10, sticky=W)

lbl_regnr = Label(vindu, text='Regnr')
lbl_regnr.grid(row=4, column=0, padx=10, pady=10, sticky=W)

lbl_hylle = Label(vindu, text='Hylle')
lbl_hylle.grid(row=5, column=0, padx=10, pady=10, sticky=W)

lbl_svar = Label(vindu, text='')
lbl_svar.grid(row=1, column=2)

nr = StringVar()
ent_nr = Entry(vindu, width=11, textvariable=nr)
ent_nr.grid(row=0, column=1, padx=10, pady=10, sticky=W)

fornavn = StringVar()
ent_fornavn = Entry(vindu, width=11, textvariable=fornavn)
ent_fornavn.grid(row=1, column=1, padx=10, pady=10, sticky=W)

etter = StringVar()
ent_etter = Entry(vindu, width=20, textvariable=etter)
ent_etter.grid(row=2, column=1, padx=10, pady=10, sticky=W)

epost = StringVar()
ent_epost = Entry(vindu, width=25, textvariable=epost)
ent_epost.grid(row=3, column=1, padx=10, pady=10, sticky=W)

regnr = StringVar()
ent_regnr = Entry(vindu, width=8, textvariable=regnr)
ent_regnr.grid(row=4, column=1, padx=10, pady=10, sticky=W)

hylle = StringVar()
ent_hylle = Entry(vindu, width=6, textvariable=hylle)
ent_hylle.grid(row=5, column=1, padx=10, pady=10, sticky=W)

btn_sjekk = Button(vindu, text='Sjekk kunde', command=sjekk_kunde)
btn_sjekk.grid(row=0, column=2, padx=10, pady=10, sticky=E)

btn_avslutt = Button(vindu, text='Avslutt', command=vindu.destroy)
btn_avslutt.grid(row=5, column=1, padx=10, pady=10, sticky=SE)

btn_lagre=Button(vindu,text='Lagre', command=lagre_info)
btn_lagre.grid(row=5,column=2,padx=10,pady=10,sticky=SE)

vindu.mainloop()

mindatabase.close()
