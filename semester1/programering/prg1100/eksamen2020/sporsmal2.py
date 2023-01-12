bildic={}

bilfil=open('bil.txt','r',encoding='utf-8')

regnr=bilfil.readline()

while regnr != '':
    regnr=regnr.rstrip('\n')
    merke=bilfil.readline().rstrip('\n')
    modell=bilfil.readline().rstrip('\n')
    startdato=bilfil.readline().rstrip('\n')
    posisjon=bilfil.readline().rstrip('\n')

    bildic[regnr]={'merke': merke,'modell':modell,'startdato':startdato,'posisjon':posisjon}

    regnr=bilfil.readline()

bilfil.close()

nyRunde='j'
while nyRunde== 'j':
    oppgittRegnr=input('Oppgi regnr du ønsker utskrift på: ')
    print(bildic[oppgittRegnr]['merke'],bildic[oppgittRegnr]['modell'],bildic[oppgittRegnr]['startdato'])

    nyRunde=input('Ønsker du ny utskrift j/n: ')