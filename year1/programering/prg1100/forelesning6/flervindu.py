from tkinter import*


def vindu_2():
    vindu2 = Toplevel()
    vindu2.title('applikasjonsvindu-vindu2')

    btn_tilbake2 = Button(
        vindu2, text='tilbake til hovedvindu', command=vindu2.destroy, fg='light blue', bg='purple')
    btn_tilbake2.grid(row=2, column=6, padx=5, pady=25, sticky=E)


def vindu_3():
    vindu3 = Toplevel()
    vindu3.title('applikasjonsvindu-vindu3')

    btn_tilbake2 = Button(
        vindu3, text='tilbake til hovedvindu', command=vindu3.destroy, bg='light blue')
    btn_tilbake2.grid(row=2, column=6, padx=5, pady=25, sticky=E)


def vindu_4():
    vindu4 = Toplevel()
    vindu4.title('applikasjonsvindu-vindu4')

    btn_tilbake2 = Button(
        vindu4, text='tilbake til hovedvindu', command=vindu4.destroy, bg='light blue')
    btn_tilbake2.grid(row=2, column=6, padx=5, pady=25, sticky=E)


def main():
    hovedvindu = Tk()
    hovedvindu.title('hovedvindu')

    btn_vindu2 = Button(hovedvindu, text='vindu2',
                        command=vindu_2, bg='purple')
    btn_vindu2.grid(row=0, column=0, padx=5, pady=5, sticky=W)

    btn_vindu3 = Button(hovedvindu, text='vindu3',
                        command=vindu_3, bg='purple')
    btn_vindu3.grid(row=0, column=1, padx=5, pady=5, sticky=W)

    btn_vindu4 = Button(hovedvindu, text='vindu4',
                        command=vindu_4, bg='purple')
    btn_vindu4.grid(row=0, column=2, padx=5, pady=5, sticky=W)

    btn_avslutt = Button(hovedvindu, text='avslutt',
                         command=hovedvindu.destroy, bg='red')
    btn_avslutt.grid(row=2, column=4, padx=5, pady=25, sticky=E)

    hovedvindu.mainloop()


main()
