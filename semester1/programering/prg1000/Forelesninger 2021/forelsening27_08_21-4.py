#program2-17 side 82, alternativ fremgangsmåte 2
#bruk av variable som holder orden på gjenværende sekunder etter konvertering

#Gjøre om fra sekunder til timer, minutter og sekunder

#ber brukeren oppgi antall sekunder
antall_sekunder=int(input('oppgi antall sekunder som skal konverteres: '))

#beregner antall timer
antall_timer=antall_sekunder//3600
resterende_sekunder_etter_timer=antall_sekunder%3600

#beregner antall gjenværende minutter og sekunder
antall_minutter=resterende_sekunder_etter_timer//60
resterende_sekunder_etter_minutter=resterende_sekunder_etter_timer%60


#utskrift av resultat
print(antall_sekunder,'sekunder gjortr om til timer, minutter og sekunder blir: ')
print('Timer',antall_timer)
print('minutter',antall_minutter)
print('Sekunder',resterende_sekunder_etter_minutter)




#hvordam løser programmet i boka problemstillingen?
