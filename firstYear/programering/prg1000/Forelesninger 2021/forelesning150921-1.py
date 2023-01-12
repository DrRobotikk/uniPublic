#Program for å beregne farge på tall på ruletten

# Alternativ 3, tar utg pkt i hvilke farger gjelder for hvilke intervaller og "talltype"

#! en test på farge, dvs sann/usann på if-test nr 3
#Kan da ikke si om tallet er partall eller oddetall eller hvilket intervall det tilhører, kun fargen

#Brukeren oppgir verdi på ruletten
tall=int(input('Hva er tallet på ruletten? '))

#Tester om gyldig verdi og beregner riktig farge for gyldige verdier
if tall >= 0 and tall<=36:
    if tall==0:
        print('Tallet er markert "Grønn" på ruletten')
    else:
        #Hele if-setningen deles over flere linjer, må da stå i ekstra ()
        if ((tall>=1 and tall<=10 and (tall%2)==0)
        or (tall>=11 and tall<=18 and (tall%2)!=0)
        or (tall>=19 and tall<=28 and (tall%2)==0)
        or (tall>=29 and tall<=36 and (tall%2)!=0)):
            print('Tallet er markert "Sort" på ruletten')
        else:
            print('Tallet er markert "Rødt på ruletten')

else:
    print('Oppgi en gyldig verdi på ruletten')

print('Program avsluttet')
