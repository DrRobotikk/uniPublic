tall1 = int(input('legg inn et tall '))
tall2 = int(input('legg inn et tall '))
tall3 = int(input('legg inn et tall '))
tall4 = int(input('legg inn et tall '))
tall5 = int(input('legg inn et tall '))
tall6 = int(input('legg inn et tall '))
tall7 = int(input('legg inn et tall '))

storst = 0
total_sum = tall1 + tall2 + tall3 + tall4 + tall5 +  tall6 + tall7

if tall1 >= storst:
    storst = tall1
else:
    storst = 0

if tall2 >= storst:
    storst = tall2
else:
    storst = tall1

if tall3 >= storst:
    storst = tall3
else:
    storst = tall2

if tall4 >= storst:
    storst = tall4
else:
    storst = tall3

if tall5 >= storst:
    storst = tall5
else:
    storst = tall4

if tall6 >= storst:
    storst = tall6
else:
    storst = tall5

if tall7 >= storst:
    storst = tall7
else:
    storst = tall6

print('Det største tallet er ',storst,'og den totale summen er ',total_sum)
