# Ber om et tall mellom 1 og 10 fra brukeren
tall = int(input('Legg inn et tall mellom 1 og 10 '))
# analyserer bruker input og gir tilbake tilsvarende tall i Romersk stil
if tall < 0:
    print('Tallet er negativt og ikke gyldig')
else:
    if tall == 1:
        print('Det romerske tallet for 1 er I')
    else:
        if tall == 2:
            print('Det romerske tallet for 2 er II')
        else:
            if tall == 3:
                print('Det romerske tallet for 3 er III')
            else:
                if tall == 4:
                    print('Det romerske tallet for 4 er IV')
                else:
                    if tall == 5:
                        print('Det romerske tallet for 5 er V')
                    else:
                        if tall == 6:
                            print('Det romerske tallet for 6 er VI')
                        else:
                            if tall == 7:
                                print('Det romerske tallet for 7 er VII')
                            else:
                                if tall == 8:
                                    print('Det romerske tallet for 8 er VIII')
                                else:
                                    if tall == 9:
                                        print('Det romerske tallet for 9 er IX')
                                    else:
                                        if tall == 10:
                                            print(
                                                'Det romerske tallet for 10 er X')
                                        else:
                                            print(
                                                'Jeg sa et tall mellom 1 og 10!!!!!!')
