from tkinter import*
import mysql.connector


def hent_info(event):
    valgt=lstOpptatt.get(lstOpptatt.curselection())

    funnet=False
    radnr=0

    while (funnet==False) and (radnr<=len(dataliste)-1):
        if valgt[0]==dataliste[radnr][0]:
            infoOm.set(dataliste[radnr][2]+' '+dataliste[radnr][3]+' '+dataliste[radnr][4])
            funnet=True
        else:
            radnr+=1


mindatabase=mysql.connector.connect(host='localhost',port=3306,user='Bilsjef',passwd='eksamen2020',db='Bildeling')

dataliste=[]

hentmarkor=mindatabase.cursor()

hentmarkor.execute(''' SELECT Utleie.Regnr,Utlevert,Kunde.Mobilnr,Fornavn,Etternavn
                       FROM Utleie JOIN Kunde
                       ON Utleie.Mobilnr=Kunde.Mobilnr
                       WHERE Innlevert IS NULL
    ''')

for rad in hentmarkor:
    dataliste+=[[rad[0],rad[1],rad[2],rad[3],rad[4]]]

hentmarkor.close()

selectdataliste=[]

for n in range(len(dataliste)):
    selectdataliste+=[[dataliste[n][0],dataliste[n][1]]]



window=Tk()
window.title('Opptatte biler')

y_scroll=Scrollbar(window,orient=VERTICAL)
y_scroll.grid(row=0, column=2, rowspan=5, padx=(0, 100), pady=5, sticky=NS)

innholdIliste=StringVar()
lstOpptatt=Listbox(window,width=30,height=5,listvariable=innholdIliste,yscrollcommand=y_scroll.set)
lstOpptatt.grid(row=0,column=1,rowspan=5,padx=(100,0),pady=5,sticky=E)
innholdIliste.set(tuple(selectdataliste))
y_scroll['command']=lstOpptatt.yview



infoOm=StringVar()
entInfo=Entry(window,width=45,state='readonly',textvariable=infoOm)
entInfo.grid(row=0,column=3,sticky=E)
lstOpptatt.bind('<<ListboxSelect>>',hent_info)


window.mainloop()



mindatabase.close()