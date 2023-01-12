# PRogram for å skrive 3 nye navn til en eksisterende fil

# Åpner fila student.txt
studentfil = open('student.txt', 'a')

# Skriver 3 nye navn til fila
studentfil.write('Olivia\n')
studentfil.write('Oline\n')
studentfil.write('Petrus\n')

# Stenger fila
studentfil.close()
