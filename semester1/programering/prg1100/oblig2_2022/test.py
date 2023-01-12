
import mysql.connector
from tkinter import*

mindatabase = mysql.connector.connect(
    host='localhost', port=3306, user='Eksamenssjef', passwd='oblig2022', db='oblig2022')




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

    sql=('SELECT Studentnr,karakter FROM Eksamensresultat WHERE Emnekode=%s AND Dato=%s AND Karakter IS NULL')

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
    btnLagre.grid(row=len(hentetliste)+1,column=4,padx=5,pady=5,sticky=E)
    
    for x in range(len(varliste)):
        varliste[x][0].set(hentetliste[x][0])

    hentMarkor.close()   



karakterregvindu=Toplevel()
karakterregvindu.title('lagring av karakterer')

lblEmnekode=Label(karakterregvindu,text='Emnekode:')
lblEmnekode.grid(row=0,column=0,padx=5,pady=5,sticky=E)

ekode=StringVar()
entEmnekode=Entry(karakterregvindu,width=7,textvariable=ekode)
entEmnekode.grid(row=0,column=1,padx=5,pady=5,sticky=W)

lblDato=Label(karakterregvindu,text='Dato:')
lblDato.grid(row=1,column=0,padx=5,pady=5,sticky=E)

date=StringVar()
entDato=Entry(karakterregvindu,width=9,textvariable=date)
entDato.grid(row=1,column=1,padx=5,pady=5,sticky=W)

btnHentEksamen=Button(karakterregvindu,text='Hent eksamen',command=hent_eksamen)
btnHentEksamen.grid(row=2,column=0,columnspan=2,padx=5,pady=5,sticky=EW)










window.mainloop()





mindatabase.close()