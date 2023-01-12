# Introduksjon til GUI-programer
# MEd komponentene ledetekst, inndatafelt , utdatafelt, knapp
from tkinter import*
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


window.mainloop()
