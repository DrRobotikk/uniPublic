#PRG1100-2022-innstikksortering - pseudo
# Program for å innstikksortere en usortert liste
# Pseudokode på algoritmen fra https://en.wikipedia.org/wiki/Insertion_sort
# for i ← 1 to length(A)
#    j ← i
#    while j > 0 and A[j-1] > A[j]
#        swap A[j] and A[j-1]
#        j ← j - 1
#    end while
# end for


talliste = []
antall_tall = int(input('Hvor mange tall skal du ha ? '))

for n in range(0, antall_tall, 1):
    tall = int(input('Legg inn tall '))
    talliste += [tall]

liste_lengde = len(talliste)

for i in range(1, liste_lengde, 1):
    indeks = i
    flyttes = 0
    print('Vi tar et "kort"')
    while indeks > 0 and talliste[indeks-1] > talliste[indeks]:
        bytte = talliste[indeks]
        talliste[indeks] = talliste[indeks-1]
        talliste[indeks-1] = bytte
        print('"kort" nr', indeks+1, 'med verdi ', talliste[indeks-1])
        flyttes = flyttes+1
        indeks = indeks-1
        print('flyttes', flyttes, 'gang(er) bortover')


print(talliste)
