#Sett variabel for løkke
ny_beregning = "ja"

while ny_beregning == "ja":
    #Skaff informasjonen vi trenger i form av input
    kjopsum = int(input('Oppgi prisen på bolig du søker lån for: '))
    egenkapital = int(input('Oppgi din egen kapital: '))
    brutto = int(input('Oppgi din bruttolønn: '))
#Beregne andre variabler
    kapital_prosent = egenkapital/kjopsum
    max_laan = brutto*5
    
#Sjekke om verdiene er gode nok for et lån
    if kapital_prosent >= 0.15 and max_laan >= kjopsum:
        print('Lånet kan bevilges')
    else:
        if kapital_prosent < 0.15:
            print('Du har for liten egen kapital for å få invilget lånet')
        if max_laan < kjopsum:
            print('Du trenger en høyere bruttolønn for å få invilget lånet')
    #Spør om løkken skal gjenta seg 
    ny_beregning = input('Ønsker du en ny beregning, svar ja eller nei: ')
   


