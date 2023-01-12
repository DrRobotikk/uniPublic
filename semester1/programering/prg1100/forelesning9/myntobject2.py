import random


class Mynt:
    def __init__(self, sideopp):
        self.__sideopp = sideopp

    def kast(self):
        if random.randint(0, 1) == 0:
            self.__sideopp = 'Krone'
        else:
            self.__sideopp = 'Mynt'

    def hent_sideopp(self):
        return self.__sideopp


def main():
    antallKron = 0
    antallMynt = 0

    sideopp = input('Hvilken side er opp?: ')

    minMynt = Mynt(sideopp)

    print('Før første kast er denne siden opp', minMynt.hent_sideopp())

    antallKast = int(input('Hvor mange kast skal du ha?: '))

    for antallGanger in range(1, antallKast+1, 1):
        minMynt.kast()
        print('Resultatet av kast nr', antallGanger,
              'ble', minMynt.hent_sideopp())
        if minMynt.hent_sideopp() == 'Krone':
            antallKron += 1
        else:
            antallMynt += 1
    print('Resultatet:', antallKron, 'antall krone og ', antallMynt, 'antall mynt')


main()
