#Importerer bibiloteket en trenger
from tkinter import*

#Lager funksjonen for å sjekke forlegg
def beregn_forelegg():
    fartsgrense = 70

    din_fart=int(malt_hastighet.get())

    if din_fart >= (fartsgrense+35):
        forelegg=9950
    else:
        if din_fart >= (fartsgrense+25):
            forelegg=6250
        else:
            if din_fart >= (fartsgrense+15):
                forelegg=3300
            else:
                if din_fart >= (fartsgrense+5):
                    forelegg=750
                else:
                    forelegg='Ingen'
    if forelegg == 'Ingen':
        forelegg_ut.set(0)
    else:
        forelegg_ut.set(forelegg) 



#Lager vinduet
window=Tk()

window.title('Fartsbotkalkulator')

#Lager de nødvendige Label og Entrys en tregner
lbl_malt_hastighet=Label(window, text='Målt hastighet/din fart i km/t:')
lbl_malt_hastighet.grid(row=0,column=0,padx=10,pady=15)

malt_hastighet=StringVar()
ent_malt_hastighet=Entry(window, width=5, textvariable=malt_hastighet)
ent_malt_hastighet.grid(row=0,column=1,padx=10,pady=15)

btn_beregn_forelegg=Button(window, text='Beregn forelegg', command=beregn_forelegg)
btn_beregn_forelegg.grid(row=0,column=2,padx=100, pady=15)

lbl_forelegg=Label(window, text='Forelegg:')
lbl_forelegg.grid(row=1,column=0,padx=10,pady=15)

forelegg_ut=StringVar()
ent_forelegg=Entry(window, width=6, state='readonly',textvariable=forelegg_ut)
ent_forelegg.grid(row=1,column=1,padx=10,pady=15)

btn_avslutt=Button(window, text='Avslutt', command=window.destroy)
btn_avslutt.grid(row=2,column=2,padx=100,pady=15)




#Setter vidnuet i løkke
window.mainloop()