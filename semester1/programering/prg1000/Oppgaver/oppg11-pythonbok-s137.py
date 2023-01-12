# få bruker input

gutter = int(input('Hvor mange gutter er det i klassen? '))
jenter = int(input('Hvor mange jenter er det i klassen? '))

# beregne klasse totalen
klasse_total = gutter+jenter

# finne ut antall prosent
prosent_av_gutter = gutter/klasse_total*100
prosent_av_jenter = jenter/klasse_total*100

print('Det er', prosent_av_gutter, 'prosent av gutter i klassen')
print('Det er', prosent_av_jenter, 'prosent av jenter i klassen')
