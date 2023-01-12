def main():
    funnet = False
    sok = input('Hva søker du etter: ')
    coffe_file = open('coffe.txt', 'r')
    beskrivelse = coffe_file.readline()

    while beskrivelse != '':
        kvantitet = coffe_file.readline().rstrip('\n')
        beskrivelse = beskrivelse.rstrip('\n')

        if beskrivelse == sok:
            print(beskrivelse)
            print(kvantitet)
            funnet = True
        beskrivelse = coffe_file.readline()
    coffe_file.close()
    if not funnet:
        print('Finnes ikke i liste')


main()
