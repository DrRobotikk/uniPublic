# utregninger og beregneringer med aksjer

# input for akjse kjøp med pris og komisjon
aksje_kjopt = float(input('Hvor mange aksjer skal du ha? '))
aksje_pris1 = float(input('Hva er prisen på aksjene? '))
prosent_til_komisjon = float(input('Hva er prosenten til megleren? '))

# beregne pris på aksje og komisjon
aksje_total1 = aksje_kjopt*aksje_pris1
komisjon1 = prosent_til_komisjon*aksje_total1/100

# beregne den totale kostnaden
total_kostnad = aksje_total1+komisjon1

# utskrift av kostnad og komisjon
print('totalt bruk er', total_kostnad, 'og komisjone alene er:', komisjon1)

# Beregne beløp og komisjon ved salg av aksjer
aksje_pris2 = float(input('Hva selges aksjene for? '))
aksje_salg = aksje_kjopt*aksje_pris2
komisjon2 = prosent_til_komisjon*aksje_salg/100

# print totale salg og komisjon av salg
print('total ved salg er', aksje_salg, 'og komisjone er', komisjon2)
total = total_kostnad+komisjon2

# beregne total verdi
verdi = aksje_salg-total

print('Du sitter igjen med', verdi, '$')
