import sporsmal4
import pickle



fortsette=True
kundedatfil=open('kunde.dat','rb')

while fortsette == True:
    try:
        kunden=pickle.load(kundedatfil)

        print(kunden.get_mobilnr(),kunden.get_etternavn(),kunden.get_epost())
    
    except EOFError:
        fortsette=False