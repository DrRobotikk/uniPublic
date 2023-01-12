import os


def main():
    funnet=False

    sok=input('Hva ønsker du å slette: ')

    coffefil=open('coffe.txt','r')
    temp_fil=open('temp.txt','w')

    beskrivelse=coffefil.readline()

    while beskrivelse != '':
        beskrivelse=beskrivelse.rstrip('\n')
        kvantitet=coffefil.readline().rstrip('\n')

        if beskrivelse != sok:
            temp_fil.write(beskrivelse+'\n')
            temp_fil.write(kvantitet+'\n')
        else:
            funnet=True
        beskrivelse=coffefil.readline()
    coffefil.close()
    temp_fil.close()

    os.remove('coffe.txt')
    os.rename('temp.txt','coffe.txt')

    if funnet:
        print('Fila er oppdatert')
    else:
        print('Det ble ikke funnet i fila')

main()        
