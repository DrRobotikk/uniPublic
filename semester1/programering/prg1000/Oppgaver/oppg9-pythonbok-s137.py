import math
# Få radiusen av brukeren
bruker_radius = float(input('Legg inn radiusen til en sirkel: '))

# beregner arealet av sirkelen
areal_av_sirkel = math.pi*bruker_radius**2

# beregner omkrets av sirkelen
omkrets_av_sirkel = 2*math.pi*bruker_radius

print('arealet av sirkelen er:', areal_av_sirkel, '\n',
      'omkretsen av sirkelen er:', omkrets_av_sirkel)
