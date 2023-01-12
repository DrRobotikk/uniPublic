
from tkinter import *


def hent_info(event):
    valgt = lst_studenter.get(lst_studenter.curselection())

    funnet = False
    radnr = 0

    while (funnet == False) and (radnr <= len(studenter)-1):
        if valgt[0] == studenter[radnr][0]:
            info_til.set(studenter[radnr][1] + ' '+studenter[radnr]
                         [2] + ' ' + studenter[radnr][3] + ' ' + studenter[radnr][6])
            print(valgt, studenter[radnr][0], studenter[radnr][2])
            funnet = True
        else:
            radnr += 1


studenter = []

studentfil = open('studenter.txt', 'r', encoding='UTF-8')

studentnr = studentfil.readline()

while studentnr != '':
    studentnr = studentnr.rstrip('\n')
    fornavn = studentfil.readline().rstrip('\n')
    etternavn = studentfil.readline().rstrip('\n')
    epost = studentfil.readline().rstrip('\n')
    fodselsdato = studentfil.readline().rstrip('\n')
    kjonn = studentfil.readline().rstrip('\n')
    studium = studentfil.readline().rstrip('\n')

    studenter += [[studentnr, fornavn, etternavn,
                   epost, fodselsdato, kjonn, studium]]
    studentnr = studentfil.readline()

studentfil.close()

student = []
for listelengde in range(0, len(studenter), 1):
    student += [[studenter[listelengde][0], studenter[listelengde][2]]]

window = Tk()
window.title('studenter')

y_scroll = Scrollbar(window, orient=VERTICAL)
y_scroll.grid(row=0, column=2, rowspan=5, padx=(0, 100), pady=5, sticky=NS)

innhold_i_lst_studenter = StringVar()
lst_studenter = Listbox(window, width=10, height=5,
                        listvariable=innhold_i_lst_studenter, yscrollcommand=y_scroll.set)
lst_studenter.grid(row=0, column=1, rowspan=5, padx=(100, 0), pady=5, sticky=E)
innhold_i_lst_studenter.set(tuple(student))
y_scroll['command'] = lst_studenter.yview

info_til = StringVar()
ent_info = Entry(window, width=45, state='readonly', textvariable=info_til)
ent_info.grid(row=0, column=3, sticky=E)
lst_studenter.bind('<<ListboxSelect>>', hent_info)


window.mainloop()
