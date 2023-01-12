#Hent tkinter 
from tkinter import*

#Lag beregnings funksjonen
def beregn_porto():
    vekt=int(forsendelsesvekt.get())
    if vekt <= 20:
        porto=17
    elif vekt<=50:
        porto=24
    elif vekt<=100:
        porto=27
    elif vekt<=350:
        porto=45
    elif vekt<=1000:
        porto=88
    else:
        porto=125
    porto_ut.set(porto)
    









#Lag vinduet
window=Tk()

#Legg til titlen
window.title('portokalkulator')

#Lager de forskjellige delene av vinduet
lbl_forsendelse=Label(window, text='forsendelsens vekt(i gram):')
lbl_forsendelse.grid(row=0,column=0, padx=100,pady=15)

forsendelsesvekt=StringVar()
ent_forsendelse=Entry(window, width=5, textvariable=forsendelsesvekt)
ent_forsendelse.grid(row=0, column=1,padx=100,pady=15)

btn_beregnporto=Button(window, text='Beregn porto', command=beregn_porto)
btn_beregnporto.grid(row=0,column=2, padx=100,pady=15)

lbl_porto=Label(window, text='Porto:')
lbl_porto.grid(row=1,column=0,padx=100,pady=15)

porto_ut=StringVar()
ent_porto=Entry(window, width=4, state='readonly', textvariable=porto_ut)
ent_porto.grid(row=1,column=1, padx=100,pady=15)

btn_avslutt=Button(window, text='Avslutt',command=window.destroy)
btn_avslutt.grid(row=2,column=2,padx=100,pady=15)

#Setter vinduet i en løkke
window.mainloop()
