from tkinter import*
import mysql.connector
import studentklasseoblig


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


def henter_studentnr():
    studliste = []
    hentMarkor = mindatabase.cursor()

    hentMarkor.execute('SELECT MAX(Studentnr) FROM Student')

    for row in hentMarkor:
        studliste += [row[0]]

    studnr = int(studliste[0])+1

    hentMarkor.close()

    return studnr


def lager_student_object():
    studentnr = henter_studentnr()

    fornavn = fnavn.get()
    etternavn = enavn.get()
    eposten = epost.get()
    telefon = tlf.get()

    nyStudent = studentklasseoblig.Student(
        studentnr, fornavn, etternavn, eposten, telefon)

    return nyStudent


def lagre_student():
    nystudent = lager_student_object()

    status, liste = sjekk_student(nystudent.get_telefon)

    if status == False:
        settinnMarkor = mindatabase.cursor()

        sql = (
            'INSERT INTO Student(Studentnr,Fornavn,Etternavn,Epost,Telefon) VALUES(%s,%s,%s,%s,%s)')

        data = (nystudent.get_studentnr(), nystudent.get_fornavn(
        ), nystudent.get_etternavn(), nystudent.get_epost(), nystudent.get_telefon())

        settinnMarkor.execute(sql, data)
        mindatabase.commit()


mindatabase = mysql.connector.connect(
    host='localhost', port=3306, user='Eksamenssjef', passwd='oblig2022', db='oblig2022')


windowRegStud = Tk()
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

btnLagre = Button(windowRegStud, text='Lagre', command=lagre_student)
btnLagre.grid(row=4, column=2, padx=5, pady=5, sticky=SE)

btnTilbake = Button(windowRegStud, text='Tilbake',
                    command=windowRegStud.destroy)
btnTilbake.grid(row=4, column=3, padx=5, pady=5, sticky=SW)

windowRegStud.mainloop()
mindatabase.close()
