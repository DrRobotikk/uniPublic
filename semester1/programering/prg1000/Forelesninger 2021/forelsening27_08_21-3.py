#program2-17 side 82, alternativ fremgangsmåte 1
#bruk av variable som holder orden på gjenværende sekunder etter en konvertering

#gjør om fra sekunder til timer, minutter og sekunder

#ber brukeren oppgi antall sekunder
antall_sekunder=int(input('oppgi antall sekunder som skal koverteres: '))

#beregner antall timer
antall_timer=antall_sekunder//3600
resterende_sekunder_etter_timer=antall_sekunder-3600*antall_timer

#beregner antall gjenværende minutter og sekunder
antall_minutter=resterende_sekunder_etter_timer//60
resterende_sekunder_etter_minutter=resterende_sekunder_etter_timer-60*antall_minutter

#utskrift av resultat
print(antall_sekunder,'sekunder gjort om til timer, minutter og sekunder blir:')
print('timer:',antall_timer)
print('minutter:',antall_minutter)
print('sekunder:',resterende_sekunder_etter_minutter)

