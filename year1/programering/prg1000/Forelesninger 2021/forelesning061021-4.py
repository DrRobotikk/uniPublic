# Første og siste element i en liste skal bytte plass
talliste = [5, 3, 2, 1, 4]
print('Lista før byttet er ', talliste)
print('Første og siste element i lista sakl bytte plass')
print()

# bytte er byttevariablen vi bruker for å ta vare på første verdi
bytte = talliste[0]

# talliste av 0 får verdien til talliste av 4
talliste[0] = talliste[4]

# talliste av 4 får verdien som vi tok vare på i byttevariablen
talliste[4] = bytte

# lista etter byttet er

print('Lista etter byttet er', talliste)
