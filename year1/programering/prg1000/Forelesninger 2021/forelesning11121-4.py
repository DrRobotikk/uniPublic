# Introduksjon til GUI-programer
# MEd komponentene ledetekst, inndatafelt , utdatafelt, knapp
# Så legger vi til kode for å foreta beregningene
# Variable må knyttes til inndatafeltene og utdatafeltene og må gjøres før plassering grid

from tkinter import*


def beregn_lan():
    if (int(egenkapital.get())/int(kjopesum.get())) >= 0.35:
        lanetilsagn.set('Lån innvilges')
    else:
        lanetilsagn.set('Lån innvilgies ikke')


window = Tk()

# Vi gir vinduet et navn
window.title('Lånekalkulator billån')

# Vi lager ledetekster for kjøpesum egenkapital og lånetilsagn
lbl_kjopesum = Label(window, text='Kjøpesum')
lbl_kjopesum.grid(row=0, column=0, padx=100, pady=15)

lbl_egenkapital = Label(window, text='Egenkapital')
lbl_egenkapital.grid(row=1, column=0, padx=100, pady=15)

lbl_lanetilsagn = Label(window, text='Lånetilsagn')
lbl_lanetilsagn.grid(row=3, column=0, padx=100, pady=15)

# Vi lager inndatafelt for Kjøpesum og Egenkapital
kjopesum = StringVar()
ent_kjopesum = Entry(window, width=9, textvariable=kjopesum)
ent_kjopesum.grid(row=0, column=1, padx=100, pady=15)

egenkapital = StringVar()
ent_egenkapital = Entry(window, width=9, textvariable=egenkapital)
ent_egenkapital.grid(row=1, column=1, padx=100, pady=15)

# Vi lager knapp for å beregne lånetilsagnet
btn_beregn = Button(window, text='Beregn lånetilsagn', command=beregn_lan)
btn_beregn.grid(row=2, column=0, columnspan=2, pady=15)

# OG vi lager et utdatafelt/visningsfelt for konklusjonen for lånetilsagnet
lanetilsagn = StringVar()
ent_lanetilsagn = Entry(
    window, width=20, state='readonly', textvariable=lanetilsagn)
ent_lanetilsagn.grid(row=3, column=1, padx=100, pady=15)


window.mainloop()
