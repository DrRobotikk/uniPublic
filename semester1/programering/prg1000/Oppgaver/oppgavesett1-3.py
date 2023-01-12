#Få din karakter

poeng = int(input('Hva er poengscoren din ? '))

if poeng >= 92:
    print('Din karakter er A')
else:
    if poeng >= 77:
        print('Din karakter er B')
    else:
        if poeng >= 58:
            print('Din karakter er  C')
        else:
            if poeng >= 46:
                print('Din karakter er D')
            else:
                if poeng >= 40:
                    print('Din karakter er E')
                else:
                    print('Din karakter er F')
