from tkinter import*
import mysql.connector
import studentklasseoblig

mindatabase = mysql.connector.connect(
    host='localhost', port=3306, user='Eksamenssjef', passwd='oblig2022', db='oblig2022')


def hent_student():
    liste = []
    hentMarkor = mindatabase.cursor()

    sql = ('''SELECT * 
            FROM Student
            WHERE Studentnr=%s 
        ''')

    hentMarkor.execute(sql % studnr.get())

    for row in hentMarkor:
        liste += [row[0], row[1], row[2], row[3], row[4]]

    hentMarkor.close()

    return liste


def lag_object():
    liste = hent_student()
    studentnr = liste[0]
    fornavn = liste[1]
    etternavn = liste[2]
    epost = liste[3]
    telefon = liste[4]

    nyStudent = studentklasseoblig.Student(
        studentnr, fornavn, etternavn, epost, telefon)

    return nyStudent


def set_info():
    student = lag_object()

    fnavn.set(student.get_fornavn())
    enavn.set(student.get_etternavn())
    epost.set(student.get_epost())
    tlf.set(student.get_telefon())


def endre_info():
    student = lag_object()

    student.set_etternavn(enavn.get())
    student.set_epost(epost.get())
    student.set_telefon(tlf.get())

    return student


def lagre_endring():
    student = endre_info()
    endreMarkor = mindatabase.cursor()

    sql = ('''
        UPDATE Student SET Etternavn=%s,Epost=%s,Telefon=%s WHERE Studentnr=%s 
        ''')

    data = (student.get_etternavn(), student.get_epost(),
            student.get_telefon(), student.get_studentnr())

    endreMarkor.execute(sql, data)
    mindatabase.commit()
    endreMarkor.close()


window = Tk()
window.title('Endre student')

lblStudnr = Label(window, text='Studentnr:')
lblStudnr.grid(row=0, column=0, padx=5, pady=5, sticky=E)

lblFornavn = Label(window, text='Fornavn:')
lblFornavn.grid(row=1, column=0, padx=5, pady=5, sticky=E)

lblEtternavn = Label(window, text='Etternavn:')
lblEtternavn.grid(row=2, column=0, padx=5, pady=5, sticky=E)

lblEpost = Label(window, text='E-post:')
lblEpost.grid(row=3, column=0, padx=5, pady=5, sticky=E)

lblTelefon = Label(window, text='Telefon:')
lblTelefon.grid(row=4, column=0, padx=5, pady=5, sticky=E)

studnr = StringVar()
entStudnr = Entry(window, width=8, textvariable=studnr)
entStudnr.grid(row=0, column=1, padx=5, pady=5, sticky=W)

fnavn = StringVar()
entFnavn = Entry(window, width=30,
                 textvariable=fnavn, state='readonly')
entFnavn.grid(row=1, column=1, padx=5, pady=5, sticky=W)

enavn = StringVar()
entEnavn = Entry(window, width=20,
                 textvariable=enavn)
entEnavn.grid(row=2, column=1, padx=5, pady=5, sticky=W)

epost = StringVar()
entEpost = Entry(window, width=40, textvariable=epost)
entEpost.grid(row=3, column=1, padx=5, pady=5, sticky=W)

tlf = StringVar()
entTlf = Entry(window, width=8, textvariable=tlf)
entTlf.grid(row=4, column=1, padx=5, pady=5, sticky=W)

btnTilbake = Button(window, text='Tilbake',
                    command=window.destroy)
btnTilbake.grid(row=5, column=3, padx=5, pady=5, sticky=SE)

btnLagre = Button(window, text='Lagre', command=lagre_endring)
btnLagre.grid(row=5, column=2, padx=5, pady=5, sticky=SE)

btnHentInfo = Button(window, text='hent info', command=set_info)
btnHentInfo.grid(row=0, column=2, padx=5, pady=5, sticky=W)


window.mainloop()
mindatabase.close()
