class Vare:
    def __init__(self,varenr,varenavn,pris,katnr,antall,hylle):
        self.__varenr=varenr
        self.__varenavn=varenavn
        self.__pris=pris
        self.__katnr=katnr
        self.__antall=antall
        self.__hylle=hylle
    
    def get_varenr(self):
        return self.__varenr
    
    def get_varenavn(self):
        return self.__varenavn
    
    def get_pris(self):
        return self.__pris

    def get_katnr(self):
        return self.__katnr

    def get_antall(self):
        return self.__antall

    def get_hylle(self):
        return self.__hylle
    