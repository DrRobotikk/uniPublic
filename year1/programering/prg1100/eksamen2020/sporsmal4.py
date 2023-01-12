from tkinter import*
import mysql.connector


def hent_info(event):
    valgt=lstOpptatt.get(lstOpptatt.curselection())

    legginnmarkor=mindatabase.cursor

    sql=('INSERT INTO Utleie')

  


mindatabase=mysql.connector.connect(host='localhost',port=3306,user='Bilsjef',passwd='eksamen2020',db='Bildeling')

ledigliste=[]


hentmarkor=mindatabase.cursor()

hentmarkor.execute('''SELECT Regnr FROM Utleie WHERE Innlevert IS NOT NULL ''')

for row in hentmarkor:
    ledigliste+=[[row[0]]]

hentmarkor.close()





window=Tk()
window.title('Opptatte biler')

y_scroll=Scrollbar(window,orient=VERTICAL)
y_scroll.grid(row=0, column=2, rowspan=5, padx=(0, 100), pady=5, sticky=NS)

innholdIliste=StringVar()
lstOpptatt=Listbox(window,width=30,height=5,listvariable=innholdIliste,yscrollcommand=y_scroll.set)
lstOpptatt.grid(row=0,column=1,rowspan=5,padx=(100,0),pady=5,sticky=E)
innholdIliste.set(tuple(ledigliste))
y_scroll['command']=lstOpptatt.yview



infoOm=StringVar()
lblmobilnr=Label(window,text='Mobilnr')
lblmobilnr.grid(row=0,column=2,padx=5,pady=5,sticky=E)
entmobilnr=Entry(window,width=11,textvariable=infoOm)
entmobilnr.grid(row=0,column=3,sticky=E)
lstOpptatt.bind('<<ListboxSelect>>',hent_info)


window.mainloop()



mindatabase.close()