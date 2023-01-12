import mysql.connector
from tkinter import*



mindatabase = mysql.connector.connect(
    host='localhost', port=3306, user='Eksamenssjef', passwd='oblig2022', db='oblig2022')


def sjekk_student(sjekk_studentInfo):
    sjekkMarkor = mindatabase.cursor()

    sjekkMarkor.execute('SELECT * FROM Student')
    studentliste = []

    for i in sjekkMarkor:
        studentliste += [i]

    funnet = False
    rad = 0

    while (funnet == False) and (rad <= len(studentliste)-1):
        if sjekk_studentInfo == studentliste[rad][4] or sjekk_studentInfo == studentliste[rad][0]:
            funnet = True

        rad += 1
    sjekkMarkor.close()
    return funnet, studentliste


def registrer_student_window():
    def legg_til_student():
        fornavn = fnavn.get()
        etternavn = enavn.get()
        eposten = epost.get()
        telefon = tlf.get()

        status, liste = sjekk_student(telefon)

        if status == False:
            studnrMarkor = mindatabase.cursor()

            studnrListe = []
            studnrMarkor.execute('SELECT MAX(Studentnr) FROM Student')

            for row in studnrMarkor:
                studnrListe += [row[0]]

            nyttStudnr = int(studnrListe[0])+1
            settInnMarkor = mindatabase.cursor()

            settInn = (
                'INSERT INTO Student(Studentnr,Fornavn,Etternavn,Epost,Telefon) VALUES(%s,%s,%s,%s,%s)')

            data = (nyttStudnr, fornavn, etternavn, eposten, telefon)

            settInnMarkor.execute(settInn, data)
            mindatabase.commit()
            settInnMarkor.close()
            studnrMarkor.close()

            lblregistrert = Label(
                windowRegStud, text='Studenten er registrert')
            lblregistrert.grid(row=4, column=1, padx=5, pady=5, sticky=E)
        if status == True:
            lblFeil = Label(
                windowRegStud, text='En student med dette nr er allerede registrert')
            lblFeil.grid(row=4, column=1, padx=5, pady=5, sticky=E)
        
        fnavn.set("")
        enavn.set("")
        epost.set("")
        tlf.set("")
        

    windowRegStud = Toplevel()
    windowRegStud.title('Registrer student')

    lblFornavn = Label(windowRegStud, text='Fornavn:')
    lblFornavn.grid(row=0, column=0, padx=5, pady=5, sticky=E)

    lblEtternavn = Label(windowRegStud, text='Etternavn:')
    lblEtternavn.grid(row=1, column=0, padx=5, pady=5, sticky=E)

    lblEpost = Label(windowRegStud, text='E-post:')
    lblEpost.grid(row=2, column=0, padx=5, pady=5, sticky=E)

    lblTelefon = Label(windowRegStud, text='Telefon:')
    lblTelefon.grid(row=3, column=0, padx=5, pady=5, sticky=E)

    fnavn = StringVar()
    entFnavn = Entry(windowRegStud, width=30, textvariable=fnavn)
    entFnavn.grid(row=0, column=1, padx=5, pady=5, sticky=W)

    enavn = StringVar()
    entEnavn = Entry(windowRegStud, width=20, textvariable=enavn)
    entEnavn.grid(row=1, column=1, padx=5, pady=5, sticky=W)

    epost = StringVar()
    entEpost = Entry(windowRegStud, width=40, textvariable=epost)
    entEpost.grid(row=2, column=1, padx=5, pady=5, sticky=W)

    tlf = StringVar()
    entTelefon = Entry(windowRegStud, width=8, textvariable=tlf)
    entTelefon.grid(row=3, column=1, padx=5, pady=5, sticky=W)

    btnLagre = Button(windowRegStud, text='Lagre', command=legg_til_student)
    btnLagre.grid(row=4, column=2, padx=5, pady=5, sticky=SE)

    btnTilbake = Button(windowRegStud, text='Tilbake',
                        command=windowRegStud.destroy)
    btnTilbake.grid(row=4, column=3, padx=5, pady=5, sticky=SW)


def lager_info(lager_infoStudnr):

    status, infoliste = sjekk_student(lager_infoStudnr)

    if status == True:
        for e in range(len(infoliste)):
            if lager_infoStudnr == infoliste[e][0]:
                fnavn = infoliste[e][1]
                enavn = infoliste[e][2]
                epost = infoliste[e][3]
                tlf = infoliste[e][4]

                return fnavn, enavn, epost, tlf


def rediger_student_window():
    def hent_info():
        fornavn, etternavn, eposten, telefon = lager_info(studnr.get())

        fnavn.set(fornavn)
        enavn.set(etternavn)
        epost.set(eposten)
        tlf.set(telefon)

    def lagre_info():
        studentnr = studnr.get()
        eposten = epost.get()
        telefon = tlf.get()

        lagreMarkor = mindatabase.cursor()

        oppdater = ('UPDATE Student SET Epost=%s,Telefon=%s WHERE Studentnr=%s')

        data = (eposten, telefon, studentnr)

        lagreMarkor.execute(oppdater, data)

        mindatabase.commit()
        lagreMarkor.close()

        lblSuksess = Label(windowrediger, text='Oppdatering utført')
        lblSuksess.grid(row=5, column=1, padx=5, pady=5, sticky=E)

    windowrediger = Toplevel()
    windowrediger.title('Rediger student info')

    lblStudnr = Label(windowrediger, text='Studentnr:')
    lblStudnr.grid(row=0, column=0, padx=5, pady=5, sticky=E)

    lblFornavn = Label(windowrediger, text='Fornavn:')
    lblFornavn.grid(row=1, column=0, padx=5, pady=5, sticky=E)

    lblEtternavn = Label(windowrediger, text='Etternavn:')
    lblEtternavn.grid(row=2, column=0, padx=5, pady=5, sticky=E)

    lblEpost = Label(windowrediger, text='E-post:')
    lblEpost.grid(row=3, column=0, padx=5, pady=5, sticky=E)

    lblTelefon = Label(windowrediger, text='Telefon:')
    lblTelefon.grid(row=4, column=0, padx=5, pady=5, sticky=E)

    studnr = StringVar()
    entStudnr = Entry(windowrediger, width=8, textvariable=studnr)
    entStudnr.grid(row=0, column=1, padx=5, pady=5, sticky=W)

    fnavn = StringVar()
    entFnavn = Entry(windowrediger, width=30,
                     textvariable=fnavn, state='readonly')
    entFnavn.grid(row=1, column=1, padx=5, pady=5, sticky=W)

    enavn = StringVar()
    entEnavn = Entry(windowrediger, width=20,
                     textvariable=enavn, state='readonly')
    entEnavn.grid(row=2, column=1, padx=5, pady=5, sticky=W)

    epost = StringVar()
    entEpost = Entry(windowrediger, width=40, textvariable=epost)
    entEpost.grid(row=3, column=1, padx=5, pady=5, sticky=W)

    tlf = StringVar()
    entTlf = Entry(windowrediger, width=8, textvariable=tlf)
    entTlf.grid(row=4, column=1, padx=5, pady=5, sticky=W)

    btnTilbake = Button(windowrediger, text='Tilbake',
                        command=windowrediger.destroy)
    btnTilbake.grid(row=5, column=3, padx=5, pady=5, sticky=SE)

    btnLagre = Button(windowrediger, text='Lagre', command=lagre_info)
    btnLagre.grid(row=5, column=2, padx=5, pady=5, sticky=SE)

    btnHentInfo = Button(windowrediger, text='hent info', command=hent_info)
    btnHentInfo.grid(row=0, column=2, padx=5, pady=5, sticky=W)


def slett_student_window():
    def hent_info():
        fornavn, etternavn, eposten, telefon = lager_info(studnr.get())

        fnavn.set(fornavn)
        enavn.set(etternavn)
        epost.set(eposten)
        tlf.set(telefon)

    def slett():
        slettMarkor = mindatabase.cursor()

        sql = ('DELETE FROM Student WHERE Studentnr=%s')
        data = [studnr.get()]

        slettMarkor.execute(sql, data)
        mindatabase.commit()
        slettMarkor.close()
        lblFullfort = Label(slettwindow, text='Student slettet')
        lblFullfort.grid(row=6, column=1, padx=5, pady=5, sticky=E)

    def spor_om_sletting():
        
        resultatliste=[]
        henteMarkor=mindatabase.cursor()
        funnet=False
        sql=('SELECT* FROM Eksamensresultat')

        henteMarkor.execute(sql)

        for row in henteMarkor:
            resultatliste+=[[row[0],row[1],str(row[2]),row[3]]]
        
        
        
        for i in range(len(resultatliste)):
            if studnr.get()==resultatliste[i][0]:
                funnet=True
        
        if funnet == True:
            lblkanIkke=Label(slettwindow,text='Studenten kan ikke slettes')
            lblkanIkke.grid(row=6,column=0,padx=5,pady=5,sticky=W)
        else:
            lblSikker = Label(
                slettwindow, text='Er du sikker på at du vil slette denne studenten?')
            lblSikker.grid(row=6, column=0, padx=5, pady=5, sticky=E)

            btnJa = Button(slettwindow, text='Ja', command=slett)
            btnJa.grid(row=6, column=1, columnspan=2, padx=5, pady=5, sticky=W)

            btnNei = Button(slettwindow, text='Nei', command=slettwindow.destroy)
            btnNei.grid(row=6, column=2, columnspan=2, padx=5, pady=5, sticky=W)

    slettwindow = Toplevel()
    slettwindow.title('Slett en student')

    lblStudnr = Label(slettwindow, text='Studentnr:')
    lblStudnr.grid(row=0, column=0, padx=5, pady=5, sticky=E)

    lblFornavn = Label(slettwindow, text='Fornavn:')
    lblFornavn.grid(row=1, column=0, padx=5, pady=5, sticky=E)

    lblEtternavn = Label(slettwindow, text='Etternavn:')
    lblEtternavn.grid(row=2, column=0, padx=5, pady=5, sticky=E)

    lblEpost = Label(slettwindow, text='E-post:')
    lblEpost.grid(row=3, column=0, padx=5, pady=5, sticky=E)

    lblTelefon = Label(slettwindow, text='Telefon:')
    lblTelefon.grid(row=4, column=0, padx=5, pady=5, sticky=E)

    studnr = StringVar()
    entStudnr = Entry(slettwindow, width=8, textvariable=studnr)
    entStudnr.grid(row=0, column=1, padx=5, pady=5, sticky=W)

    fnavn = StringVar()
    entFnavn = Entry(slettwindow, width=30,
                     textvariable=fnavn, state='readonly')
    entFnavn.grid(row=1, column=1, padx=5, pady=5, sticky=W)

    enavn = StringVar()
    entEnavn = Entry(slettwindow, width=20,
                     textvariable=enavn, state='readonly')
    entEnavn.grid(row=2, column=1, padx=5, pady=5, sticky=W)

    epost = StringVar()
    entEpost = Entry(slettwindow, width=40,
                     textvariable=epost, state='readonly')
    entEpost.grid(row=3, column=1, padx=5, pady=5, sticky=W)

    tlf = StringVar()
    entTlf = Entry(slettwindow, width=8, textvariable=tlf, state='readonly')
    entTlf.grid(row=4, column=1, padx=5, pady=5, sticky=W)

    btnTilbake = Button(slettwindow, text='Tilbake',
                        command=slettwindow.destroy)
    btnTilbake.grid(row=5, column=3, padx=5, pady=5, sticky=SE)

    btnSlett = Button(slettwindow, text='Slett', command=spor_om_sletting)
    btnSlett.grid(row=5, column=2, padx=5, pady=5, sticky=SE)

    btnHentInfo = Button(slettwindow, text='hent info', command=hent_info)
    btnHentInfo.grid(row=0, column=2, padx=5, pady=5, sticky=W)


def eksamen_leggTil_vindu():
    def sjekk_rom():
        emnekode = ekode.get()
        dato = date.get()
        romNr=rNr.get()

        eksamenMarkor = mindatabase.cursor()

        sql = (
            'SELECT Romnr FROM Eksamen WHERE Emnekode=%s  AND Dato=%s ')
        data = (emnekode,dato)

        eksamenMarkor.execute(sql, data)
        

        liste = []

        for row in eksamenMarkor:
            liste += [row[0]]
        
        
        
        if len(liste)<1 :
            oppdaterMarkor=mindatabase.cursor()
            

            settinn=('INSERT INTO Eksamen(Emnekode,Dato,Romnr) VALUES(%s,%s,%s)')
            data=(emnekode,dato,romNr)

            oppdaterMarkor.execute(settinn,data)
            mindatabase.commit()
            lbllagttil=Label(eksamenWindow,text='Eksamen er lagt til')
            lbllagttil.grid(row=3,column=0,padx=5,pady=5,sticky=W)

            oppdaterMarkor.close()
        if len(liste)>=1:
            lblopptatt=Label(eksamenWindow,text='Rommet er opptatt')
            lblopptatt.grid(row=3,column=0,padx=5,pady=5,sticky=W)

        eksamenMarkor.close()

    eksamenWindow = Toplevel()
    eksamenWindow.title('Legg til en eksamen')

    lblEmnekode = Label(eksamenWindow, text='Emnekode:')
    lblEmnekode.grid(row=0, column=0, padx=5, pady=5, sticky=E)

    lblDato = Label(eksamenWindow, text='Dato:')
    lblDato.grid(row=1, column=0, padx=5, pady=5, sticky=E)

    lblRomnr = Label(eksamenWindow, text='Romnr:')
    lblRomnr.grid(row=2, column=0, padx=5, pady=5, sticky=E)

    ekode = StringVar()
    entEkode = Entry(eksamenWindow, width=8, textvariable=ekode)
    entEkode.grid(row=0, column=1, padx=5, pady=5, sticky=W)

    date = StringVar()
    entDato = Entry(eksamenWindow, width=10, textvariable=date)
    entDato.grid(row=1, column=1, padx=5, pady=5, sticky=W)

    rNr = StringVar()
    entRomnr = Entry(eksamenWindow, width=4, textvariable=rNr)
    entRomnr.grid(row=2, column=1, padx=5, pady=5, sticky=W)

    btnLeggInn = Button(eksamenWindow, text='Legg til', command=sjekk_rom)
    btnLeggInn.grid(row=3, column=1, padx=5, pady=5, sticky=SE)

    btnTilbake = Button(eksamenWindow, text='Tilbake',
                        command=eksamenWindow.destroy)
    btnTilbake.grid(row=3, column=2, padx=5, pady=5, sticky=SE)


def rediger_eksamen_vindu():
    def endre_romnr():
        emnekode=ekode.get()
        dato=date.get()
        romnr=rNr.get()






        oppdaterMarkor=mindatabase.cursor()

        sql=('UPDATE Eksamen SET Romnr=%s WHERE Emnekode=%s AND Dato=%s')

        data=(romnr,emnekode,dato)

        oppdaterMarkor.execute(sql,data)
        mindatabase.commit()
        
    def hent_romnr():
        emnekode=ekode.get()
        dato=date.get()

        romliste=[]

        hentRomnrMarkor=mindatabase.cursor()

        sql=('SELECT Romnr FROM Eksamen WHERE Emnekode=%s AND Dato=%s')

        data=(emnekode,dato)

        hentRomnrMarkor.execute(sql,data)


        

        for row in hentRomnrMarkor:
            romliste+=[row[0]]
        hentRomnrMarkor.close()
        
        rNr.set(romliste[0])

    redigerEksamenVindu=Toplevel()
    redigerEksamenVindu.title('Rediger Eksamen')

    lblEmnekode = Label(redigerEksamenVindu, text='Emnekode:')
    lblEmnekode.grid(row=0, column=0, padx=5, pady=5, sticky=E)

    lblDato = Label(redigerEksamenVindu, text='Dato:')
    lblDato.grid(row=1, column=0, padx=5, pady=5, sticky=E)

    lblRomnr = Label(redigerEksamenVindu, text='Romnr:')
    lblRomnr.grid(row=2, column=0, padx=5, pady=5, sticky=E)

    ekode = StringVar()
    entEkode = Entry(redigerEksamenVindu, width=8, textvariable=ekode)
    entEkode.grid(row=0, column=1, padx=5, pady=5, sticky=W)

    date = StringVar()
    entDato = Entry(redigerEksamenVindu, width=10, textvariable=date)
    entDato.grid(row=1, column=1, padx=5, pady=5, sticky=W)

    rNr = StringVar()
    entRomnr = Entry(redigerEksamenVindu, width=5, textvariable=rNr)
    entRomnr.grid(row=2, column=1, padx=5, pady=5, sticky=W)

    btnHentRomnr=Button(redigerEksamenVindu,text='Hent romnr',command=hent_romnr)
    btnHentRomnr.grid(row=2,column=2,padx=5,pady=5,sticky=W)

    btnEndring=Button(redigerEksamenVindu,text='Lagre endring',command=endre_romnr)
    btnEndring.grid(row=3,column=2,padx=5,pady=5,sticky=E)

    btnTilbake=Button(redigerEksamenVindu,text='Tilbake',command=redigerEksamenVindu.destroy)
    btnTilbake.grid(row=3,column=3,padx=5,pady=5,sticky=E)


def Karakterliste_emne_vindu():
    def karakterStatestikk():
        tekstbox.config(state=NORMAL)
        tekstbox.delete('1.0','end')
        emnekode=ekode.get()
        dato=date.get()



        hentMarkor=mindatabase.cursor()

        sql=('SELECT Emne.Emnenavn,eksamensresultat.Dato,eksamensresultat.Karakter,COUNT(eksamensresultat.Karakter) AS Antall FROM eksamensresultat JOIN emne ON eksamensresultat.Emnekode=Emne.Emnekode WHERE Emne.Emnekode=%s AND Eksamensresultat.Dato=%s AND Karakter IS NOT NULL GROUP BY Emne.Emnenavn,eksamensresultat.Dato,eksamensresultat.Karakter ORDER BY karakter')
        
        data=emnekode,dato
        
        hentMarkor.execute(sql,data)

        karakterliste=[]

        
        for row in hentMarkor:
            karakterliste += [[row[0],str(row[1]),row[2],str(row[3])]]
        
        for i in karakterliste:
            tekstbox.insert(END,i[0]+" "+i[1]+" "+i[2]+" "+i[3]+'\n')
        tekstbox.config(state=DISABLED)

        
        
    karakterEmnewindow = Toplevel()
    karakterEmnewindow.title('Karakterutskrift for oppgitt eksamen')

    lblemneKode = Label(karakterEmnewindow, text='Emnekode:')
    lblemneKode.grid(row=0, column=0, padx=5, pady=5, sticky=W)

    lbldato=Label(karakterEmnewindow,text='Dato:')
    lbldato.grid(row=1,column=0,padx=5,pady=5,sticky=W)

    ekode = StringVar()
    entemne = Entry(karakterEmnewindow, width=9, textvariable=ekode)
    entemne.grid(row=0, column=1, padx=5, pady=5, sticky=W)

    date=StringVar()
    entDato=Entry(karakterEmnewindow,width=9,textvariable=date)
    entDato.grid(row=1,column=1,padx=5,pady=5,sticky=W)

    tekstbox=Text(karakterEmnewindow,width=50,height=10)
    tekstbox.grid(row=0,column=2,padx=5,pady=5,sticky=NS)

    btnHentKarakter=Button(karakterEmnewindow,text='Hent karakterstatestikk', command=karakterStatestikk)
    btnHentKarakter.grid(row=2,column=1,padx=5,pady=5,sticky=W)

    btnTilbake=Button(karakterEmnewindow,text='Tilbake',command=karakterEmnewindow.destroy)
    btnTilbake.grid(row=2,column=4,padx=5,pady=5,sticky=E)


def karakter_student_vindu():
    def hent_karakter():
        tekstbox.config(state=NORMAL)
        tekstbox.delete('1.0','end')
        Studentnr=studnr.get()

        hentMarkor=mindatabase.cursor()

        sql=('SELECT eksamensresultat.Studentnr,Emne.emnenavn,eksamensresultat.Dato,Eksamensresultat.Karakter FROM eksamensresultat JOIN emne ON eksamensresultat.Emnekode=emne.Emnekode WHERE Studentnr=%s AND Karakter IS NOT NULL')

        hentMarkor.execute(sql%Studentnr)
        karakterliste=[]

        for row in hentMarkor:
            karakterliste+=[[row[0],row[1],str(row[2]),row[3]]]
        hentMarkor.close()
        

        for i in karakterliste:
            tekstbox.insert(END,i[0]+" "+i[1]+" "+i[2]+" "+i[3]+'\n')
        tekstbox.config(state=DISABLED)


    karakterStudentvindu=Toplevel()
    karakterStudentvindu.title('Utskrift av karakter for oppgitt student')

    lblstudnr=Label(karakterStudentvindu,text='Studentnr:')
    lblstudnr.grid(row=0,column=0,padx=5,pady=5,sticky=E)

    studnr=StringVar()
    entStudnr=Entry(karakterStudentvindu,width=6,textvariable=studnr)
    entStudnr.grid(row=0,column=1,padx=5,pady=5,sticky=W)

    btnHentKarakter=Button(karakterStudentvindu,text='Hent karakterer', command=hent_karakter)
    btnHentKarakter.grid(row=1,column=0,padx=5,pady=5,sticky=W)

    btnTilbake=Button(karakterStudentvindu,text='Tilbake',command=karakterStudentvindu.destroy)
    btnTilbake.grid(row=1,column=4,padx=5,pady=5,sticky=E)

    tekstbox=Text(karakterStudentvindu,width=50,height=10)
    tekstbox.grid(row=0,column=2,padx=5,pady=5,sticky=NS)

def karakterstatestikk_student_vindu():
    def hent_statestikk():
        tekstbox.config(state=NORMAL)
        tekstbox.delete('1.0',END)


        emnekode=ekode.get()
        dato=date.get()
        resultaltliste=[]

        resultatMarkor=mindatabase.cursor()

        sql=('SELECT Studentnr, Emne.Emnenavn,eksamensresultat.Dato,eksamensresultat.Karakter FROM eksamensresultat JOIN emne ON eksamensresultat.Emnekode=Emne.Emnekode WHERE Emne.Emnekode=%s AND Eksamensresultat.Dato=%s AND Karakter IS NOT NULL GROUP BY Studentnr, Emne.Emnenavn,eksamensresultat.Dato,eksamensresultat.Karakter ORDER BY Studentnr')

        data=(emnekode,dato)

        resultatMarkor.execute(sql,data)

        for row in resultatMarkor:
            resultaltliste+=[[row[0],row[1],str(row[2]),row[3]]]

        print(resultaltliste)

        for i in resultaltliste:
            tekstbox.insert(END, i[0]+" "+i[1]+" "+i[2]+" "+i[3]+'\n')
        tekstbox.config(state=DISABLED)


    studentkaraktervindu=Toplevel()
    studentkaraktervindu.title('Utskrift av eksamensresultat med studenter')

    lblemne=Label(studentkaraktervindu,text='Emnekode:')
    lblemne.grid(row=0,column=0,padx=5,pady=5,sticky=E)

    ekode=StringVar()
    entEmne=Entry(studentkaraktervindu,width=7,textvariable=ekode)
    entEmne.grid(row=0,column=1,padx=5,pady=5,sticky=W)


    lbldato=Label(studentkaraktervindu,text='Dato:')
    lbldato.grid(row=1,column=0,padx=5,pady=5,sticky=E)

    date=StringVar()
    entdate=Entry(studentkaraktervindu,width=9,textvariable=date)
    entdate.grid(row=1,column=1,padx=5,pady=5,sticky=W)

    tekstbox=Text(studentkaraktervindu,width=50,height=10)
    tekstbox.grid(row=0,rowspan=10,column=2,padx=5,pady=5,sticky=NS)

    btnhentstatestikk=Button(studentkaraktervindu,text='Hent statestikk',command=hent_statestikk)
    btnhentstatestikk.grid(row=2,column=0,padx=5,pady=5,sticky=W)

    btnTilbake=Button(studentkaraktervindu,text='Tilbake',command=studentkaraktervindu.destroy)
    btnTilbake.grid(row=11,column=3,padx=5,pady=5,sticky=E)


def eksamneinfo_vindu():
    def hent_liste_periode():
        tekstbox.config(state=NORMAL)
        tekstbox.delete('1.0','end')
        datoFra=dateFra.get()
        datoTil=dateTil.get()

        hentMarkor=mindatabase.cursor()

        sql=('SELECT Eksamen.Emnekode,Emne.Emnenavn,Emne.Studiepoeng,Eksamen.Romnr FROM Eksamen JOIN emne ON Eksamen.Emnekode=Emne.Emnekode WHERE Dato  BETWEEN %s AND %s')

        data=(datoFra,datoTil)

        hentMarkor.execute(sql,data)
        eksamenliste=[]
        for row in hentMarkor:
            eksamenliste+=[[row[0],row[1],(str(row[2])),row[3]]]
        hentMarkor.close()




        for i in eksamenliste:
            tekstbox.insert(END,i[0]+" "+i[1]+" "+i[2]+" "+i[3]+'\n')
        hentMarkor.close()
        tekstbox.config(state=DISABLED)
    
    def hent_liste_dato():
        tekstbox.config(state=NORMAL)
        tekstbox.delete('1.0','end')
        dato=date.get()
        hentMarkor=mindatabase.cursor()

        sql=("SELECT Eksamen.Emnekode,Emne.Emnenavn,Emne.Studiepoeng,Eksamen.Romnr FROM Eksamen JOIN emne ON Eksamen.Emnekode=Emne.Emnekode WHERE Dato=%s")
        data=(dato,)

        hentMarkor.execute(sql,data)
        eksamenliste=[]
        for row in hentMarkor:
            eksamenliste+=[[row[0],row[1],(str(row[2])),row[3]]]
        
        hentMarkor.close()



        for i in eksamenliste:
            tekstbox.insert(END,i[0]+" "+i[1]+" "+i[2]+" "+i[3]+'\n')
        tekstbox.config(state=DISABLED)
        hentMarkor.close()



    eksameninfovindu=Toplevel()
    eksameninfovindu.title('Utskrift av eksamener på oppgitt dag eller oppgitt periode')


    tekstbox=Text(eksameninfovindu,width=50,height=30)
    tekstbox.grid(row=0,column=0,padx=5,pady=5,sticky=NS)

    lblDatoFra=Label(eksameninfovindu,text='Dato fra:')
    lblDatoFra.grid(row=0,column=2,padx=5,pady=5,sticky=W)

    dateFra=StringVar()
    entDatoFra=Entry(eksameninfovindu,width=9,textvariable=dateFra)
    entDatoFra.grid(row=0,column=3,padx=5,pady=5,sticky=E)

    lblTil=Label(eksameninfovindu,text='Til:')
    lblTil.grid(row=0,column=4,padx=5,pady=5,sticky=W)

    dateTil=StringVar()
    entDatoTil=Entry(eksameninfovindu,width=9,textvariable=dateTil)
    entDatoTil.grid(row=0,column=5,padx=5,pady=5,sticky=W)

    lblDato=Label(eksameninfovindu,text='Dato:')
    lblDato.grid(row=1,column=2,padx=5,pady=5,sticky=E)

    date=StringVar()
    entdato=Entry(eksameninfovindu,width=9,textvariable=date)
    entdato.grid(row=1,column=3,padx=5,pady=5,sticky=W)


    btnhentDato=Button(eksameninfovindu,text='Hent eksamener for oppgitt dato',command=hent_liste_dato)
    btnhentDato.grid(row=1,column=4,columnspan=2,padx=5,pady=5,sticky=W)

    btnHentPeriode=Button(eksameninfovindu,text='Hent eksamner for oppgitt periode',command=hent_liste_periode)
    btnHentPeriode.grid(row=0,column=6,padx=5,pady=5,sticky=W)
    

    btnTilbake=Button(eksameninfovindu,text='Tilbake',command=eksameninfovindu.destroy)
    btnTilbake.grid(row=2,column=6,padx=5,pady=5,sticky=E)

def vitnemal_vindu():
    def hent_vitnemal():
        tekstbox.config(state=NORMAL)
        tekstbox.delete('1.0','end')
        Studentnr=studnr.get()


        karakterliste=[]
        studiepoeng=0



        hentkaratkerMarkor=mindatabase.cursor()


        sqlkarakter=('SELECT  Emnekode,Emnenavn, Dato,MIN(Karakter) AS Karakter,studiepoeng FROM Eksamensresultat JOIN Emne USING (Emnekode) JOIN Student USING(Studentnr) WHERE Studentnr=%s AND Karakter IS NOT NULL AND Karakter NOT LIKE "F" GROUP BY Emnekode ORDER BY Emnekode ASC  ')

        hentkaratkerMarkor.execute(sqlkarakter%Studentnr)

        for row in hentkaratkerMarkor:
            karakterliste+=[[row[0],row[1],str(row[2]),row[3],str(row[4])]]
        
        for i in range(len(karakterliste)):
            studiepoeng += float(karakterliste[i][4])


        

        

        for i in karakterliste:
            tekstbox.insert(END,i[0]+" "+i[1]+" "+i[2]+" "+i[3]+" "+i[4]+ '\n')
        tekstbox.insert(END,"Summen av Studiepoeng:"+str(studiepoeng))
        tekstbox.config(state=DISABLED)


    vitnemal_vindu=Toplevel()
    vitnemal_vindu.title('Utskrift av vitnemål for oppgitt student')

    lblstudnr=Label(vitnemal_vindu,text='Studentnr:')
    lblstudnr.grid(row=0,column=0,padx=5,pady=5,sticky=E)

    studnr=StringVar()
    entStudnr=Entry(vitnemal_vindu,width=6,textvariable=studnr)
    entStudnr.grid(row=0,column=1,padx=5,pady=5,sticky=W)

    btnHentVitnemal=Button(vitnemal_vindu,text='Hent vitnemål',command=hent_vitnemal)
    btnHentVitnemal.grid(row=1,column=0,padx=5,pady=5,sticky=W)

    btnTilbake=Button(vitnemal_vindu,text='Tilbake',command=vitnemal_vindu.destroy)
    btnTilbake.grid(row=1,column=4,padx=5,pady=5,sticky=E)

    tekstbox=Text(vitnemal_vindu,width=55,height=10)
    tekstbox.grid(row=0,column=2,padx=5,pady=5,sticky=NS)


def oppmelding_vindu():
    def legg_til_eksamensresultat():
        studentnr=studnr.get()
        emnekode=ekode.get()
        dato=date.get()

        leggtilMarkor=mindatabase.cursor()

        sql=('INSERT INTO Eksamensresultat(Studentnr,Emnekode,Dato,Karakter) VALUES(%s,%s,%s,NULL)')
        data=(studentnr,emnekode,dato)

        leggtilMarkor.execute(sql,data)
        mindatabase.commit()
        leggtilMarkor.close()

        lblregistrert=Label(oppmeldingvindu,text='Eksamensresultat lagt til')
        lblregistrert.grid(row=3,column=0,padx=5,pady=5)
    oppmeldingvindu=Toplevel()
    oppmeldingvindu.title('Oppmelding til eksamen')

    lblstudnr=Label(oppmeldingvindu,text='Studentnr:')
    lblstudnr.grid(row=0,column=0,padx=5,pady=5,sticky=E)

    studnr=StringVar()
    entStudnr=Entry(oppmeldingvindu,width=7,textvariable=studnr)
    entStudnr.grid(row=0,column=1,padx=5,pady=5,sticky=W)

    lblemne=Label(oppmeldingvindu,text='Emnekode:')
    lblemne.grid(row=1,column=0,padx=5,pady=5,sticky=E)

    ekode=StringVar()
    entEkode=Entry(oppmeldingvindu,width=7,textvariable=ekode)
    entEkode.grid(row=1,column=1,padx=5,pady=5,sticky=W)

    lblDato=Label(oppmeldingvindu,text='Dato:')
    lblDato.grid(row=2,column=0,padx=5,pady=5,sticky=E)

    date=StringVar()
    entDato=Entry(oppmeldingvindu,width=9,textvariable=date)
    entDato.grid(row=2,column=1,padx=5,pady=5,sticky=W)

    btnLeggTill=Button(oppmeldingvindu,text='Legg til',command=legg_til_eksamensresultat)
    btnLeggTill.grid(row=3,column=3,padx=5,pady=5,sticky=E)

    btnTilbake=Button(oppmeldingvindu,text='Tilbake',command=oppmeldingvindu.destroy)
    btnTilbake.grid(row=3,column=4,padx=5,pady=5,sticky=E)


def karakter_registrering_vindu():
    def hent_eksamen():
        def lagre_eksamen():
            for y in range(len(varliste)):
                lagreMarkor=mindatabase.cursor()
                karakter=varliste[y][1].get()

                sql=('UPDATE Eksamensresultat SET Karakter=%s WHERE Studentnr=%s AND Emnekode=%s AND Dato=%s')

                data=(karakter,hentetliste[y][0],emnekode,dato)

                lagreMarkor.execute(sql,data)
                mindatabase.commit()
                lagreMarkor.close()

            lblLagtTil=Label(registrervindu,text='Resultat lagret')
            lblLagtTil.grid(row=len(hentetliste)+1,column=0,padx=5,pady=5,sticky=W)

                
        registrervindu=Toplevel()
        registrervindu.title('Legg inn karakterer')

        hentMarkor=mindatabase.cursor()

        emnekode=ekode.get()
        dato=date.get()

        sql=('SELECT Studentnr,karakter FROM Eksamensresultat WHERE Emnekode=%s AND Dato=%s AND Karakter IS NULL ORDER BY Studentnr')

        data=(emnekode,dato)

        hentMarkor.execute(sql,data)

        

        hentetliste=[]
        varliste=[]

        for row in hentMarkor:
            hentetliste+=[[row[0],row[1]]]
        
        for i in range(len(hentetliste)):
            lblStudentnr=Label(registrervindu,text='Studentnr:')
            lblStudentnr.grid(row=i,column=0,padx=5,pady=5,sticky=E)

            studnr=StringVar()
            entstudnr=Entry(registrervindu,width=7,state='readonly',textvariable=studnr)
            entstudnr.grid(row=i,column=1,padx=5,pady=5,sticky=W)

            lblKarakter=Label(registrervindu,text='Karakter:')
            lblKarakter.grid(row=i,column=3,padx=5,pady=5,sticky=E)

            kter=StringVar()
            entKarakter=Entry(registrervindu,width=2,textvariable=kter)
            entKarakter.grid(row=i,column=4,padx=5,pady=5,sticky=W)

            varliste+=[[studnr,kter]]

        btnLagre=Button(registrervindu,text='Lagre',command=lagre_eksamen)
        btnLagre.grid(row=len(hentetliste)+1,column=3,padx=5,pady=5,sticky=E)

        btnTilbake=Button(registrervindu,text='Tilbake',command=registrervindu.destroy)
        btnTilbake.grid(row=len(hentetliste)+1,column=4,padx=5,pady=5,sticky=E)
        
        for x in range(len(varliste)):
            varliste[x][0].set(hentetliste[x][0])

        hentMarkor.close()   



    karakterregvindu=Toplevel()
    karakterregvindu.title('lagring av karakterer')

    lblEmnekode=Label(karakterregvindu,text='Emnekode:')
    lblEmnekode.grid(row=0,column=0,padx=5,pady=5,sticky=E)

    ekode=StringVar()
    entEmnekode=Entry(karakterregvindu,width=8,textvariable=ekode)
    entEmnekode.grid(row=0,column=1,padx=5,pady=5,sticky=W)

    lblDato=Label(karakterregvindu,text='Dato:')
    lblDato.grid(row=1,column=0,padx=5,pady=5,sticky=E)

    date=StringVar()
    entDato=Entry(karakterregvindu,width=9,textvariable=date)
    entDato.grid(row=1,column=1,padx=5,pady=5,sticky=W)

    btnHentEksamen=Button(karakterregvindu,text='Hent eksamen',command=hent_eksamen)
    btnHentEksamen.grid(row=2,column=0,columnspan=2,padx=5,pady=5,sticky=EW)

    btnTilbake=Button(karakterregvindu,text='Tilbake',command=karakterregvindu.destroy)
    btnTilbake.grid(row=2,column=3,padx=5,pady=5,sticky=E)

def endre_eksamensresultat_vindu():

    def endre_karakter():
        karakter=karak.get()

        oppdaterMarkor=mindatabase.cursor()

        sql=('UPDATE Eksamensresultat SET Karakter=%s WHERE Studentnr=%s AND Emnekode=%s AND Dato=%s')

        data=(karakter,studnr.get(),ekode.get(),date.get())

        oppdaterMarkor.execute(sql,data)
        mindatabase.commit()
        oppdaterMarkor.close()

        lblSuksess=Label(resultatendring,text='Karakter oppdatert')
        lblSuksess.grid(row=4,column=0,padx=5,pady=5,sticky=E)
    def henter_karakter():



        studentnr=studnr.get()
        emnekode=ekode.get()
        dato=date.get()
        karakterliste=[]

        hentMarkor=mindatabase.cursor()

        sql=('SELECT Karakter FROM Eksamensresultat WHERE Studentnr=%s AND Emnekode=%s AND Dato=%s')

        data=(studentnr,emnekode,dato)

        hentMarkor.execute(sql,data)

        for row in hentMarkor:
            karakterliste+=[row[0]]
        
        karak.set(karakterliste[0])

        hentMarkor.close()

    resultatendring=Toplevel()
    resultatendring.title('Endrign av eksamensresultat')

    lblStudnr=Label(resultatendring,text='Studentnr:')
    lblStudnr.grid(row=0,column=0,padx=5,pady=5,sticky=E)

    studnr=StringVar()
    entstudnr=Entry(resultatendring,width=7,textvariable=studnr)
    entstudnr.grid(row=0,column=1,padx=5,pady=5,sticky=W)

    lblEmnekode=Label(resultatendring,text='Emnekode:')
    lblEmnekode.grid(row=1,column=0,padx=5,pady=5,sticky=E)

    ekode=StringVar()
    entEmnekode=Entry(resultatendring,width=9,textvariable=ekode)
    entEmnekode.grid(row=1,column=1,padx=5,pady=5,sticky=W)


    lblDato=Label(resultatendring,text='Dato:')
    lblDato.grid(row=2,column=0,padx=5,pady=5,sticky=E)

    date=StringVar()
    entDato=Entry(resultatendring,width=9,textvariable=date)
    entDato.grid(row=2,column=1,padx=5,pady=5,sticky=W)

    lblKarakter=Label(resultatendring,text='Karakter:')
    lblKarakter.grid(row=3,column=0,padx=5,pady=5,sticky=E)

    karak=StringVar()
    entKarakter=Entry(resultatendring,width=2,textvariable=karak)
    entKarakter.grid(row=3,column=1,padx=5,pady=5,sticky=W)

    btnHentKarakter=Button(resultatendring,text='Hent karakter',command=henter_karakter)
    btnHentKarakter.grid(row=3,column=3,padx=5,pady=5,sticky=E)

    btnLagre=Button(resultatendring,text='Lagre',command=endre_karakter)
    btnLagre.grid(row=4,column=3,padx=5,pady=5,sticky=E)

    btnTilbake=Button(resultatendring,text='Tilbake',command=resultatendring.destroy)
    btnTilbake.grid(row=4,column=4,padx=5,pady=5,sticky=E)


def slette_eksamensresultat_vindu():
    def sletter_resultat():
        slettMarkor=mindatabase.cursor()

        sql=('DELETE FROM Eksamensresultat WHERE Studentnr=%s AND Emnekode=%s AND Dato=%s')

        data=(studnr.get(),ekode.get(),date.get())

        slettMarkor.execute(sql,data)
        mindatabase.commit()
        lblslettet=Label(sletteksamenresultat,text='Resultatet er slettet')
        lblslettet.grid(row=4,column=0,padx=5,pady=5,sticky=W)

    def henter_karakter():
        studentnr=studnr.get()
        emnekode=ekode.get()
        dato=date.get()
        karakterliste=[]

        hentMarkor=mindatabase.cursor()

        sql=('SELECT Karakter FROM Eksamensresultat WHERE Studentnr=%s AND Emnekode=%s AND Dato=%s')

        data=(studentnr,emnekode,dato)

        hentMarkor.execute(sql,data)

        for row in hentMarkor:
            karakterliste+=[row[0]]
        
        karak.set(karakterliste[0])

        hentMarkor.close()
    sletteksamenresultat=Toplevel()
    sletteksamenresultat.title('Sletting av et eksamensresultat')

    lblStudnr=Label(sletteksamenresultat,text='Studentnr:')
    lblStudnr.grid(row=0,column=0,padx=5,pady=5,sticky=E)

    studnr=StringVar()
    entstudnr=Entry(sletteksamenresultat,width=7,textvariable=studnr)
    entstudnr.grid(row=0,column=1,padx=5,pady=5,sticky=W)

    lblEmnekode=Label(sletteksamenresultat,text='Emnekode:')
    lblEmnekode.grid(row=1,column=0,padx=5,pady=5,sticky=E)

    ekode=StringVar()
    entEmnekode=Entry(sletteksamenresultat,width=9,textvariable=ekode)
    entEmnekode.grid(row=1,column=1,padx=5,pady=5,sticky=W)


    lblDato=Label(sletteksamenresultat,text='Dato:')
    lblDato.grid(row=2,column=0,padx=5,pady=5,sticky=E)

    date=StringVar()
    entDato=Entry(sletteksamenresultat,width=9,textvariable=date)
    entDato.grid(row=2,column=1,padx=5,pady=5,sticky=W)

    lblKarakter=Label(sletteksamenresultat,text='Karakter:')
    lblKarakter.grid(row=3,column=0,padx=5,pady=5,sticky=E)

    karak=StringVar()
    entKarakter=Entry(sletteksamenresultat,width=2,textvariable=karak)
    entKarakter.grid(row=3,column=1,padx=5,pady=5,sticky=W)

    btnHentKarakter=Button(sletteksamenresultat,text='Hent karakter',command=henter_karakter)
    btnHentKarakter.grid(row=3,column=3,padx=5,pady=5,sticky=E)

    btnSlett=Button(sletteksamenresultat,text='Slett',command=sletter_resultat)
    btnSlett.grid(row=4,column=3,padx=5,pady=5,sticky=E)

    btnTilbake=Button(sletteksamenresultat,text='Tilbake',command=sletteksamenresultat.destroy)
    btnTilbake.grid(row=4,column=4,padx=5,pady=5,sticky=E)
    
def slett_eksamen_vindu():
    def sletter_eksamen():
        emnekode=ekode.get()
        dato=date.get()

        slettMarkor=mindatabase.cursor()

        sql=('DELETE FROM Eksamen WHERE Emnekode=%s AND Dato=%s')

        data=(emnekode,dato)

        slettMarkor.execute(sql,data)
        mindatabase.commit()

        lblSlettet=Label(sletteksamen,text='Eksamen er slettet')
        lblSlettet.grid(row=2,column=0,padx=5,pady=5,sticky=W)

    sletteksamen=Toplevel()
    sletteksamen.title('Slett en eksamen')

    lblEmnekode=Label(sletteksamen,text='Emnekode:')
    lblEmnekode.grid(row=0,column=0,padx=5,pady=5,sticky=E)

    ekode=StringVar()
    entEmnekode=Entry(sletteksamen,width=9,textvariable=ekode)
    entEmnekode.grid(row=0,column=1,padx=5,pady=5,sticky=W)

    lblDato=Label(sletteksamen,text='Dato:')
    lblDato.grid(row=1,column=0,padx=5,pady=5,sticky=E)

    date=StringVar()
    entDato=Entry(sletteksamen,width=9,textvariable=date)
    entDato.grid(row=1,column=1,padx=5,pady=5,sticky=W)

    btnSlett=Button(sletteksamen,text='Slett',command=sletter_eksamen)
    btnSlett.grid(row=2,column=4,padx=5,pady=5,sticky=E)

    btnTilbake=Button(sletteksamen,text='Tilabek',command=sletteksamen.destroy)
    btnTilbake.grid(row=2,column=5,padx=5,pady=5,sticky=E)




def main():
    window = Tk()
    window.title('Hovedmeny')

    btnRegistrerStudent = Button(
        window, text='Registrer student', command=registrer_student_window)
    btnRegistrerStudent.grid(row=0, column=0, padx=5, pady=5, sticky=W)

    btnEndreStudent = Button(window, text='rediger en student',
                            command=rediger_student_window)
    btnEndreStudent.grid(row=1, column=0, padx=5, pady=5, sticky=W)

    btnSlettStudent = Button(window, text='Slett en student',
                            command=slett_student_window)
    btnSlettStudent.grid(row=2, column=0, padx=5, pady=5, sticky=W)

    btnLeggTilEksamen = Button(
        window, text='Legg inn en eksamen', command=eksamen_leggTil_vindu)
    btnLeggTilEksamen.grid(row=0, column=1, padx=5, pady=5, sticky=W)

    btnRedigerEksamen=Button(window,text='Rediger Eksamen',command=rediger_eksamen_vindu)
    btnRedigerEksamen.grid(row=1,column=1,padx=5,pady=5,sticky=W)

    btnslettEksamen=Button(window,text='Slett eksamen',command=slett_eksamen_vindu)
    btnslettEksamen.grid(row=2,column=1,padx=5,pady=5,sticky=W)

    btnKarakterliste = Button(
        window, text='skriv ut karakterstatestikk for oppgitt Eksamen', command=Karakterliste_emne_vindu)
    btnKarakterliste.grid(row=0, column=2, padx=5, pady=5, sticky=W)

    btnkarakterstud=Button(window,text='Skriv ut karakterliste for oppgitt student',command=karakter_student_vindu)
    btnkarakterstud.grid(row=1,column=2,padx=5,pady=5,sticky=W)

    btnEksameninfo=Button(window,text='Utskrift av eksamen på oppgitt dag/periode' ,command=eksamneinfo_vindu)
    btnEksameninfo.grid(row=3,column=2,padx=5,pady=5,sticky=W)

    btnstudenteksamenresultat=Button(window,text='eksamensresultat m/studentinfo',command=karakterstatestikk_student_vindu)
    btnstudenteksamenresultat.grid(row=2,column=3,padx=5,pady=5,sticky=W)

    btnVitnemal=Button(window,text='Hent ut vitnemål for oppgitt student', command=vitnemal_vindu)
    btnVitnemal.grid(row=2,column=2,padx=5,pady=5,sticky=W)

    btnOppmelidng=Button(window,text='Oppmeld til eksamen',command=oppmelding_vindu)
    btnOppmelidng.grid(row=0,column=3,padx=5,pady=5,sticky=W)

    btnKarakterregistrering=Button(window,text='Karakter registrering',command=karakter_registrering_vindu)
    btnKarakterregistrering.grid(row=1,column=3,padx=5,pady=5,sticky=W)

    btnEndreresultat=Button(window,text='Endre eksamensresultat',command=endre_eksamensresultat_vindu)
    btnEndreresultat.grid(row=3,column=3,padx=5,pady=5,sticky=W)

    btnSlettResultat=Button(window,text='Slett eksamensresultat',command=slette_eksamensresultat_vindu)
    btnSlettResultat.grid(row=4,column=3,padx=5,pady=5,sticky=W)

    btnAvslutt=Button(window,text='Avslutt',command=window.destroy)
    btnAvslutt.grid(row=5,column=4,padx=5,pady=5,sticky=E)


    window.mainloop()

main()

mindatabase.close()
