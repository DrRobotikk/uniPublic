# PRG1100-2022-innstikksortering slightly_faster - pseudo
# Program for å innstikksortere en usortert liste
# fra https://en.wikipedia.org/wiki/Insertion_sort:
# kommentaren tar utgangspunkt i "Innstikksortering - v2021"
# After expanding the "swap" operation in-place as
# t ← A[j]; A[j] ← A[j-1]; A[j-1] ← t
# (where t is a temporary variable),
# a slightly faster version can be produced that moves A[i] to its position in one go

# and only performs one assignment in the inner loop body
# Pseudokoden blir da:
# for i = 1 to length(A)
#    x = A[i]
#    j = i - 1
#    while j >= 0 and A[j] > x
#        A[j+1] = A[j]
#        j = j - 1
#    end while
#    A[j+1] = x
# end for
# The new inner loop shifts elements to the right to clear a spot for x = A[i]

talliste = [5, 3, 1, 2, 4]
# antall_tall = int(input('Hvor mange tall skal du ha ? '))

# for n in range(0, antall_tall, 1):
#     tall = int(input('Legg inn tall '))
#     talliste += [tall]

liste_lengde = len(talliste)

print(talliste)


for i in range(1, liste_lengde, 1):
    x = talliste[i]
    j = i-1
    print('Vi jobber med "kort" nr', i+1, 'i lista over')
    print('Det har verdi ', talliste[i])
    print('"Kortet tas ut"')

    flyttet = 0
    while j >= 0 and talliste[j] > x:
        talliste[j+1] = talliste[j]
        j = j-1
        flyttet = flyttet+1

    talliste[j+1] = x
    print('og', flyttet, '"kort" foran flyttes til høyre før "kortet" settes inn')
    print('Resultat så langt er ', talliste)

print(talliste)
