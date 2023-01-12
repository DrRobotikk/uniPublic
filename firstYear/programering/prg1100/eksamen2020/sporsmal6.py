import pickle

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




bilfil=open('bil.txt','r',encoding='utf-8')
bildatfil=open('bil.dat','wb')

regnr=bilfil.readline()


while regnr != '':
    regnr=regnr.rstrip('\n')
    merke=bilfil.readline().rstrip('\n')
    modell=bilfil.readline().rstrip('\n')
    startdato=bilfil.readline().rstrip('\n')
    posisjon=bilfil.readline().rstrip('\n')

    nybil=Bil(regnr,merke,modell,startdato,posisjon)

    pickle.dump(nybil,bildatfil)

    regnr=bilfil.readline()
bilfil.close()
bildatfil.close()


fortsette=True 
bildatfil=open('bil.dat','rb')

while fortsette == True:
    try:
        bilen=pickle.load(bildatfil)

        print('posisjonen',bilen.get_posisjon())


    except EOFError:
        fortsette=False
bildatfil.close()

