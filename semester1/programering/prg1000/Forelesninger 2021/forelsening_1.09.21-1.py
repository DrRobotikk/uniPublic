#matematetiske operatorer og opertaorpresedens
#Vi bruker oppgavene i checkpoint 2.19

a=6+3*5
print('svaret i a er ',a)

b=12/2-4

print('svaret i b er ',b)

c= 9+14*2-6

print('svaret i c er',c)

d= (6+2)*3
print('svaret i d er ',d)

e=14/(11-4)
print('svaret i e er',e)

f=9+12*(8-3)
print('svaret i f er',f)

#formatering av desimaltall

pris_pr_kg=10.37
antall_kg=9.6
totalpris=antall_kg*pris_pr_kg

print('totaltprisen er: ',totalpris)

dobbel_total=2*totalpris
print('dobbel av totalpris er',dobbel_total)

#utskrift av totalpreis avrundet til 2 desimaler
print('Totalpris er',format(totalpris,'.2f'))
