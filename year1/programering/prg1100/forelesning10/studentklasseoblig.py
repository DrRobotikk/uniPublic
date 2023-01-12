class Student:
    def __init__(self, studentnr, fornavn, etternavn, epost, telefon):
        self.__studentnr = studentnr
        self.__fornavn = fornavn
        self.__etternavn = etternavn
        self.__epost = epost
        self.__telefon = telefon

    def set_etternavn(self, etternavn):
        self.__etternavn = etternavn

    def set_epost(self, epost):
        self.__epost = epost

    def set_telefon(self, telefon):
        self.__telefon = telefon

    def get_studentnr(self):
        return self.__studentnr

    def get_fornavn(self):
        return self.__fornavn

    def get_etternavn(self):
        return self.__etternavn

    def get_epost(self):
        return self.__epost

    def get_telefon(self):
        return self.__telefon

    def __str__(self):
        return self.__studentnr + '\n'+self.__fornavn+'\n'+self.__etternavn+'\n'+self.__epost+'\n'+self.__telefon
