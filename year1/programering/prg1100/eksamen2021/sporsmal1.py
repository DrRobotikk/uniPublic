kundefil=open('kunde.txt','r',encoding='utf-8')
kundeliste=[]


mobilnr=kundefil.readline()

while mobilnr!='':
    mobilnr=mobilnr.rstrip('\n')
    fornavn=kundefil.readline().rstrip('\n')
    etternavn=kundefil.readline().rstrip('\n')
    epost=kundefil.readline().rstrip('\n')

    kundeliste+=[[mobilnr,fornavn,etternavn,epost]]

    mobilnr=kundefil.readline()

kundefil.close()

for kunde in range(len(kundeliste)):
    print(kundeliste[kunde][0],kundeliste[kunde][1],kundeliste[kunde][2])