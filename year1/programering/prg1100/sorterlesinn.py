
talliste = []

antall_tall = int(input('Hvor mange tall skal du ha? '))

for n in range(0, antall_tall, 1):
    tall = int(input('Legg inn tall '))
    talliste += [tall]


print(talliste)


for n in range(0, len(talliste), 1):
    print(' da starter gjennomgang ', n+1)

    for x in range(0, len(talliste)-1, 1):
        if talliste[x] > talliste[x+1]:
            bytt = talliste[x]
            talliste[x] = talliste[x+1]
            talliste[x+1] = bytt
            print('sammenligner tall ', talliste[x], 'med tall', talliste[x+1])
            print('resultat etter byttet er ', talliste)

print('Den sorterte lista er ', talliste)
