# Program for å skrive tre navn til en ny fil

# Definerer og åpner fila student.txt
studentfil = open('student.txt', 'w')

# Skriver 3 navn til fila
# Hver tekststreng slutter med \n
studentfil.write('Torvald\n')
studentfil.write('Kari\n')
studentfil.write('Jens\n')

# Stenger fila
studentfil.close()
