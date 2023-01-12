# Beregne og sammenligne priser for leie av bil

# lag tall rekkevidden
for n in range(0, 501, 50):
    pris1 = 750
    pris2 = 300+(2*n)
    pris3 = 150+(4*n)
    if pris1 < pris2 and pris1 < pris3:
        print('Beste prisen er alternativ 1', pris1, 'på km', n)
    elif pris2 < pris3:
        print('Beste prisen er alternativ 2', pris2, 'på km', n)
    else:
        print('Beste pris er alterrnativ 3', pris3, 'på km', n)
