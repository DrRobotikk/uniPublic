import pickle


class Student:
    def __init__(self, studentnr, fornavn, etternavn, epost, studium):
        self.__studentnr = studentnr
        self.__fornavn = fornavn
        self.__etternavn = etternavn
        self.__epost = epost
        self.__studium = studium

    def set_studentnr(self, studentnr):
        self.__studentnr = studentnr

    def set_fornavn(self, fornavn):
        self.__fornavn = fornavn

    def set_etternavn(self, etternavn):
        self.__etternavn = etternavn

    def set_epost(self, epost):
        self.__epost = epost

    def set_studium(self, studium):
        self.__studium = studium

    def get_studentnr(self):
        return self.__studentnr

    def get_fornavn(self):
        return self.__fornavn

    def get_etternavn(self):
        return self.__etternavn

    def get_epost(self):
        return self.__epost

    def get_studium(self):
        return self.__studium

    def __str__(self):
        return 'objektene til klassen er:' + '\n'+self.__studentnr + '\n'+self.__fornavn+'\n'+self.__etternavn+'\n'+self.__epost+'\n'+self.__studium


studentnr = input('Oppgi studentnr: ')
fornavn = input('Oppgi fornavn: ')
etternavn = input('Oppgi etternavn: ')
epost = input('Oppgi epost: ')
studium = input('Oppgi studium: ')

nyStudent = Student(studentnr, fornavn, etternavn, epost, studium)


print(nyStudent)

print()

print(nyStudent.get_epost())
print(nyStudent.get_studium())

epost = input('Oppgi ny e-post: ')

nyStudent.set_epost(epost)

studium = input('Oppgi nytt studium: ')

nyStudent.set_studium(studium)
print()
# print(nyStudent)

studentfil = open('student.dat', 'wb')

pickle.dump(nyStudent, studentfil)

studentfil.close()

nyStudent = pickle.load(open('student.dat', 'rb'))

print(nyStudent)
