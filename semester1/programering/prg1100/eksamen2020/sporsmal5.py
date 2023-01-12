class Bil:
    def __init__(self,regnr,merke,modell,startdato,posisjon):
        self.__regnr=regnr
        self.__merke=merke
        self.__modell=modell
        self.__startdato=startdato
        self.__posisjon=posisjon

    def set_posisjon(self,posisjon):
        self.__posisjon=posisjon

    def get_posisjon(self):
        return self.__posisjon




regnr=input('Oppgi Regnr på bilen: ')
merke=input('Oppgi merke på bilen: ')
modell=input('Oppgi modell på bilen: ')
startdato=input('Oppgi startdato på bilen: ')
posisjon=input('Oppgi posisjonen på bilen: ')

nybil=Bil(regnr,merke,modell,startdato,posisjon)

print(nybil.get_posisjon())
posisjon=input('Oppgi posisjon: ')
nybil.set_posisjon(posisjon)
print(nybil.get_posisjon())

