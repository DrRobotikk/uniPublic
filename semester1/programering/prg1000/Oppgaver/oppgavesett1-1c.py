#få vite hvor mange deltakere det er
deltager = int(input('Hvor mange deltakere er det ? '))
leie_av_bane = 2500
pris_pr_deltager = 420*deltager



if deltager >= 20:
    ekstrabelop = 350*deltager
else:
    if deltager >= 10:
        ekstrabelop = 380*deltager
    else:
        ekstrabelop = 0

totalpris = leie_av_bane + pris_pr_deltager + ekstrabelop

print('Den totale prisen deres er',totalpris)

if deltager <= 9:
    baneleie = 3500
    pris_pa_deltager = 350*deltager
else:
    if deltager <=19:
        baneleie = 2000
        pris_pa_deltager = 400*deltager
    else:
        if deltager >= 20:
            baneleie = 1000
            pris_pa_deltager = 450*deltager

totalpris2 = baneleie + pris_pa_deltager

print('Den andre fulleprisen er',totalpris2)
