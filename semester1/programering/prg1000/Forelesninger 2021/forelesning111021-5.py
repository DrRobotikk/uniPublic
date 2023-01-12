# Porgram for å lese navn for navn og skrive ut de navnene  som passer med "søkekritere"
# Generell fremgangsmåte jfr fig 6-17 og program 6-9

# Åpner fila student.txt
studentfil = open('student.txt', 'r')

# Leser første linje i fila
# Ved bruk av readline-metoden
student = studentfil.readline()

# I Python, readline returnerer en tom streng('') når en leser eof-merket,
# da tester vi på det

while student != '':
    if student[0] == 'O':
        print(student.rstrip('\n'))
    # lese neste linje i fila
    student = studentfil.readline()

# stenger fila
studentfil.close()

# Prøv selv ta bort linjeskift r/strip
