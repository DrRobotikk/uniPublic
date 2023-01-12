class Student:
    def __init__(self, studentnr, fornavn, etternavn, epost, studium):
        self.__studentnr = studentnr
        self.__fornavn = fornavn
        self.__etternavn = etternavn
        self.__epost = epost
        self.__studium = studium

    def __str__(self):
        return 'objektene til klassen er:' + '\n'+self.__studentnr + '\n'+self.__fornavn+'\n'+self.__etternavn+'\n'+self.__epost+'\n'+self.__studium

    def get_fornavn(self):
        return self.__fornavn


studentnr = "123"
fornavn = 'Robin'
etternavn = 'asdfsadfsdf'
epost = 'asdfsdfsf'
studium = 'asdasdasdas'


nystudent = Student(studentnr, fornavn, etternavn, epost, studium)
print(nystudent)
