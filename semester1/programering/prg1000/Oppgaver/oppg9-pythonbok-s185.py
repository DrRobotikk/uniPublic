# Be om input fra bruker
tall = int(input('Legg inn et tall mellom 0 og 36: '))

# Bruke if statements for å finne korrekt respons
if tall < 0:
    print('Tallet er negativt og ikke godkjent')
else:
    if tall == 0:
        print('Tallet', tall, 'er grønn ')
    else:
        if tall > 36:
            print('Tallet', tall,
                  'er for høyt i forhold til det som ble bedt om!')
        else:
            if tall >= 29:
                if tall % 2 == 0:
                    print('Tallet', tall, 'er rød ')
                else:
                    print('Tallet', tall, 'er svart ')
            else:
                if tall >= 19:
                    if tall % 2 == 0:
                        print('Tallet', tall, 'er svart ')
                    else:
                        print('Tallet', tall, 'er rød ')
                else:
                    if tall >= 11:
                        if tall % 2 == 0:
                            print('Tallet', tall, 'er rød ')
                        else:
                            print('Tallet', tall, 'er svart ')
                    else:
                        if tall >= 1:
                            if tall % 2 == 0:
                                print('Tallet', tall, 'er svart ')
                            else:
                                print('Tallet', tall, 'er rød ')
