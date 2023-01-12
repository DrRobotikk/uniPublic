#få vite hvor mange deltakere det er
deltager = int(input('Hvor mange deltakere er det ? '))
leie_av_bane = 2500
pris_pr_deltager = 420*deltager



if deltager >= 10:
    ekstrabeløp = 380*deltager
else:
    ekstrabeløp = 0

totalpris = leie_av_bane + pris_pr_deltager + ekstrabeløp

print('Den totale prisen deres er',totalpris)
