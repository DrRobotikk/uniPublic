from tkinter import*

def beregn_marginalskatt():
    li=int(lonnsinntekt.get())
    if li>=964801:
        ms=0.464
    else:
        if li>=617501:
            ms=0.434
        else:
            if li>=245651:
                ms=0.344
            else:
                if li >= 224001:
                    ms=0.321
                else:
                    if li >= 174501:
                        ms=0.222
                    else:
                        if li >= 102019:
                            ms=0.203
    if li >= 102019:
        ms=ms*100
        marginalskatt.set(format(ms,'.2f'))

window=Tk()

window.title('Marginalskattkalkulator')

lbl_lonnsinntekt=Label(window, text='Lønnsinntekt:')
lbl_lonnsinntekt.grid(row=0,column=0, padx=10, pady=15)

lonnsinntekt=StringVar()
ent_lonnsinntekt=Entry(window, width=8, textvariable=lonnsinntekt)
ent_lonnsinntekt.grid(row=0, column=1, padx=10, pady=15)

btn_beregn_skattprosent=Button(window, text='Beregn marginalsakttprosent', command=beregn_marginalskatt)
btn_beregn_skattprosent.grid(row=0, column=2, padx=100, pady=15)

lbl_marginalskatt=Label(window, text='Marginalskatt:')
lbl_marginalskatt.grid(row=2,column=0, padx=10, pady=15)

marginalskatt=StringVar()
ent_marginalskatt=Entry(window, state='readonly', width=5, textvariable=marginalskatt)
ent_marginalskatt.grid(row=2, column=1, padx=10, pady=15)

btn_avslutt=Button(window, text='Avslutt', command=window.destroy)
btn_avslutt.grid(row=3, column=2, padx=100, pady=15)


window.mainloop()
