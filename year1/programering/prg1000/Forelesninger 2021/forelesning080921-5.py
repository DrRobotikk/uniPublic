# Lage ruletten med bare if-statment

tall = int(input('Legg inn et tall mellom 0 og  36: '))
partall = tall % 2 == 0

if tall == partall:
    print('Det er et partall')
if tall < 0 or tall > 36:
    print('ugyldig verdi')
if tall > 0 and tall <= 10:
    print('intervall er [1,10]')
if tall > 10 and tall <= 18:
    print('intervall er [11,18]')
if tall > 18 and tall <= 28:
    print('intervall er [19,28')
if tall > 28 and tall <= 36:
    print('intervall er [29,36]')
if tall == 0:
    print('Grønn')    
