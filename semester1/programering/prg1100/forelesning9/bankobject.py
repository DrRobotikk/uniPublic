class BankKonto:
    def __init__(self, saldo):
        self.__saldo = saldo

    def innskudd(self, belop):
        self.__saldo = self.__saldo+belop

    def uttak(self, belop):
        if self.__saldo >= belop:
            self.__saldo = self.__saldo = belop
        else:
            print('Feil. ikke nok på konto')

    def hent_saldo(self):
        return self.__saldo


def main():
    saldo = float(input('Hva er saldoen på kontoen til Kari: '))

    karisKonto = BankKonto(saldo)

    saldo = float(input('Hva er saldoen til Knut'))

    knutsKonto = BankKonto(saldo)

    belop = float(input('Hvor mye skal Kari sette inn på konto? '))

    karisKonto.innskudd(belop)

    print('saldoen på kontoen til kari er', karisKonto.hent_saldo())

    belop = float(input('Hvor mye skal Knut sette inn på konto? '))
    knutsKonto.innskudd(belop)

    print('Saldoen på kontoen til Knut er', knutsKonto.hent_saldo())

    belop = float(input('Hvor mye skal Kari ta ut fra kontoen? '))
    karisKonto.uttak(belop)

    print('Saldoen på konteon til Kari er: ', karisKonto.hent_saldo())

    belop = float(input('Hvor mye skal knut ta ut av kontoen? '))
    knutsKonto.uttak(belop)

    print('Saloden på kontoen til knut er:', knutsKonto.hent_saldo())


main()
