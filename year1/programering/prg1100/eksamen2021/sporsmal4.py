class Kunde:
    def __init__(self,mobilnr,fornavn,etternavn,epost):
        self.__mobilnr=mobilnr
        self.__fornavn=fornavn
        self.__etternavn=etternavn
        self.__epost=epost
    
    def set_epost(self,epost):
        self.__epost=epost
    
    def get_epost(self):
        return self.__epost
    
    def get_mobilnr(self):
        return self.__mobilnr

    def get_etternavn(self):
        return self.__etternavn



mobilnr=input('Oppgi mobilnr: ')
fornavn=input('Oppgi fornavn: ')
etternavn=input('Oppgi Etternavn: ')
epost=input('Oppgi epost')

nykunde=Kunde(mobilnr,fornavn,etternavn,epost)


print(nykunde.get_epost())