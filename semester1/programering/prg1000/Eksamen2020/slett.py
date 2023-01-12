import os


def slett_dekksett():
    fortsette = 'j'
    while fortsette == 'j':

        ent_regnr = input('Oppgi regnr: ')

        oppbevaringsfil = open('oppbevaring.txt', 'r')
        tempfil = open('temp.txt', 'w')
        dekksettfil = open('dekksett.txt', 'r')
        dekktemp = open('dekktemp.txt', 'w')

        opp_mobilnr = oppbevaringsfil.readline()

        while opp_mobilnr != '':
            bol_oppbevaring = False
            opp_mobilnr = opp_mobilnr.rstrip('\n')
            opp_regnr = oppbevaringsfil.readline().rstrip('\n')
            innlevering = oppbevaringsfil.readline().rstrip('\n')
            utlevering = oppbevaringsfil.readline().rstrip('\n')
            hylle = oppbevaringsfil.readline().rstrip('\n')
            pris = oppbevaringsfil.readline().rstrip('\n')

            if opp_regnr == ent_regnr and utlevering != 'x':
                bol_oppbevaring = True

            if bol_oppbevaring == False:
                tempfil.write(opp_mobilnr+'\n')
                tempfil.write(opp_regnr+'\n')
                tempfil.write(innlevering+'\n')
                tempfil.write(utlevering+'\n')
                tempfil.write(hylle+'\n')
                tempfil.write(pris+'\n')

                dekk_mobilnr = dekksettfil.readline()
                while dekk_mobilnr != '':
                    bol_dekk = False
                    dekk_mobilnr = dekk_mobilnr.rstrip('\n')
                    dekk_regnr = dekksettfil.readline().rstrip('\n')

                    if dekk_regnr == ent_regnr:
                        bol_dekk = True
                    if bol_dekk == False:
                        dekktemp.write(dekk_mobilnr+'\n'+dekk_regnr+'\n')

                    dekk_mobilnr = dekksettfil.readline()

            opp_mobilnr = oppbevaringsfil.readline()

        tempfil.close()
        oppbevaringsfil.close()
        dekksettfil.close()
        dekktemp.close()

        os.remove('oppbevaring.txt')
        os.rename('temp.txt', 'oppbevaring.txt')
        os.remove('dekksett.txt')
        os.rename('dekktemp.txt', 'dekksett.txt')

        fortsette = input('Ønsker du å slette enda et dekksett j/n: ')


slett_dekksett()
