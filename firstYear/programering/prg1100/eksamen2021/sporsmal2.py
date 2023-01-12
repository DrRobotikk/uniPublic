from tkinter import*
import mysql.connector



def hent_info(event):
    valgt=lstOpptatt.get(lstOpptatt.curselection())

    funnet=False
    radnr=0

    while (funnet==False) and (radnr<=len(dataliste)-1):
        if valgt[0]==dataliste[radnr][2]:
            infoOm.set(dataliste[radnr][0]+' '+dataliste[radnr][1]+' '+dataliste[radnr][4])
            funnet=True
        
        radnr+=1


     


mindatabse=mysql.connector.connect(host='localhost',port=3306,user='Dekksjef',passwd='Eksamen2021',db='Dekkhotell')


window=Tk()

hentdataMarkor=mindatabse.cursor()
dataliste=[]
listboxliste=[]

hentdataMarkor.execute('''SELECT Kunde.Mobilnr,etternavn,Oppbevaring.regnr,Oppbevaring.innlevert,Hylle
FROM Kunde JOIN Oppbevaring
    ON Kunde.Mobilnr=Oppbevaring.Mobilnr
WHERE Utlevert IS NULL ''')

for row in hentdataMarkor:
    dataliste+=[[row[0],row[1],row[2],row[3],row[4]]]

for n in range(len(dataliste)):
    listboxliste+=[[dataliste[n][2],dataliste[n][3]]]









y_scroll=Scrollbar(window,orient=VERTICAL)
y_scroll.grid(row=0, column=2, rowspan=5, padx=(0, 100), pady=5, sticky=NS)

innholdIliste=StringVar()
lstOpptatt=Listbox(window,width=30,height=5,listvariable=innholdIliste,yscrollcommand=y_scroll.set)
lstOpptatt.grid(row=0,column=1,rowspan=5,padx=(100,0),pady=5,sticky=E)
innholdIliste.set(tuple(listboxliste))
y_scroll['command']=lstOpptatt.yview



infoOm=StringVar()
entInfo=Entry(window,width=45,state='readonly',textvariable=infoOm)
entInfo.grid(row=0,column=3,sticky=E)
lstOpptatt.bind('<<ListboxSelect>>',hent_info)







window.mainloop()