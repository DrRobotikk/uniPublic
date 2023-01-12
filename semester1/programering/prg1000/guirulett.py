from tkinter import*


def rulett():
    tall = int(tall1.get())
    if tall == 0:
        farge.set('Grønn')
    else:
        if tall <= 10:
            if (tall % 2) == 0:
                farge.set('Sort')
            else:
                farge.set('Rødt')
        else:
            if tall <= 18:
                if (tall % 2) == 0:
                    farge.set('Rødt')
                else:
                    farge.set('Sort')
            else:
                if tall <= 28:
                    if (tall % 2) == 0:
                        farge.set('Sort')
                    else:
                        farge.set('Rødt')
                else:
                    if tall <= 36:
                        if (tall % 2) == 0:
                            farge.set('Rødt')
                        else:
                            farge.set('Sort')


window = Tk()
window.title('Rulett')


lbl_tall = Label(window, text='Tall')
lbl_tall.grid(row=0, column=0, padx=100, pady=15)

tall1 = StringVar()
ent_tall = Entry(window, width=2, textvariable=tall1)
ent_tall.grid(row=0, column=2, padx=100, pady=15)

lbl_farge = Label(window, text='Farge')
lbl_farge.grid(row=2, column=0, padx=100, pady=15)

farge = StringVar()
ent_farge = Entry(window, width=6, state='readonly', textvariable=farge)
ent_farge.grid(row=2, column=2, padx=100, pady=15)

btn_finn_farge = Button(window, text='Finn Farge', command=rulett)
btn_finn_farge.grid(row=1, column=1, padx=100, pady=15)

btn_avslutt = Button(window, text='Avslutt', command=window.destroy)
btn_avslutt.grid(row=3, column=1, padx=100, pady=15)


window.mainloop()
