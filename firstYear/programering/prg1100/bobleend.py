# PRG1100-2022-boblesortering med stoppmerke - pseudo
# Program for å boblesortere en usortert liste A
# Pseudo for boblesortering med stoppmerke
# bytte=true
# j=1
# while bytte:
#   bytte=false
#   for i=0 to length[A]-j:
#       if A[i]>A[i+1]:
#           bytte=true
#           A[i] og A[i+1] bytter plass
#       end if
#   end for
#   j=j+1
# end while

talliste = []
antall_tall = int(input('Hvor mange tall skal du ha ? '))

for n in range(0, antall_tall, 1):
    tall = int(input('Legg inn tall '))
    talliste += [tall]

bytte = True
stoppmerke = 1
liste_lengde = len(talliste)
print('Start på WHILE-løkka')
while bytte:
    bytte = False
    print('Gjennomgang starter')
    print('Start på FOR-løkka')
    for i in range(0, liste_lengde-stoppmerke, 1):
        if talliste[i] > talliste[i+1]:
            bytte = True
            byttevariabel = talliste[i]
            talliste[i] = talliste[i+1]
            talliste[i+1] = byttevariabel
            print('liste etter byttet er', talliste)
    stoppmerke = stoppmerke+1
    print('Slutt på FOR-løkka')
print('SLutt på WHILE-løkka')

print('Den sorterte lista er ', talliste)
