from tkinter import *
import mysql.connector
bdDatabase=mysql.connector.connect(host='localhost', port=3306, user='Bilsjef', passwd='eksamen2020', db='Bildeling')

## hoveddef 
def lagre():
    ### OBS VeD 2 DIMENSJONALE LISTER: Valgt[0] = første kolonne
    ## VED 1 Dimensjonale lister: Valgt[0] = Første bokstav :'D 
    valgt=lbox.get(lbox.curselection())
    regnr=valgt
    #sjekk om duplikat!
    mobilnr=mobilnr_SV.get()

    duplikat_markor=bdDatabase.cursor()

    duplikat_markor.execute('''
    SELECT Mobilnr
    FROM Utleie
    WHERE Innlevert IS NULL
    ''')

    duplikat=False

    for row in duplikat_markor:
        if row[0]==mobilnr:
            duplikat=True
    duplikat_markor.close()

    if duplikat==False:
        #finner ut kmUt
        km_markor=bdDatabase.cursor()
        km_markor.execute('''
        SELECT MAX(KmInn)
        FROM Utleie
        WHERE Regnr=%s
        ''',(regnr,))

        for row in km_markor:
            kmUt=row[0]
        print (kmUt)
        print(regnr)
        km_markor.close()

        #Insert på oppføringen
        insert_markor=bdDatabase.cursor()
        insert_markor.execute('''
        INSERT INTO Utleie VALUES
        (%s,CURRENT_TIMESTAMP,%s,%s,NULL,NULL,NULL)
        ''',(regnr,kmUt,mobilnr))

        insert_markor.close()
        bdDatabase.commit()
    else:
        print('Mobilnr har utestående utleie registrert, vennligst prøv på nytt senere')

## henter biler som er ledige 
ledige_biler=[]
ledige_biler_markor=bdDatabase.cursor()

ledige_biler_markor.execute('''
    SELECT DISTINCT Regnr
    FROM Utleie
    WHERE innlevert IS NOT NULL 
    ''')
for row in ledige_biler_markor:
    ledige_biler+=[row[0]]

## UI 
window=Tk()

#labelframes
lb_lf=LabelFrame(window,text='Ledige biler')
lb_lf.grid(row=0,column=0,padx=5,pady=5)

lb_input=LabelFrame(window,text='Brukerinfo')
lb_input.grid(row=0,column=1,padx=5,pady=5)

btn_avslutt=Button(window,text='Avslutt',width=10,command=window.destroy)
btn_avslutt.grid(row=1,column=1)

#listebox
y_scroll=Scrollbar(lb_lf,orient=VERTICAL)
y_scroll.grid(row=0,column=1,rowspan=5,padx=(0,20),pady=5,sticky=NS)

innhold_lbox=StringVar()
lbox=Listbox(lb_lf,width=50, height=5, listvariable=innhold_lbox,yscrollcommand=y_scroll.set)
lbox.grid(column=0,row=0,padx=5,pady=5)
innhold_lbox.set(ledige_biler)

y_scroll["command"]=lbox.yview

#input
mobilnr_label=Label(lb_input,text='Mobilnr:')
mobilnr_label.grid(column=0,row=0,padx=5,pady=5,sticky=W)

mobilnr_SV=StringVar()
mobilnr_ent=Entry(lb_input,width=11,textvariable=mobilnr_SV)
mobilnr_ent.grid(column=1,row=0,padx=5,pady=5,sticky=W)

btn_lagre=Button(lb_input,width=7,text='Lagre',command=lagre)
btn_lagre.grid(column=1,row=1,padx=5,pady=5,sticky=SE)

window.mainloop()