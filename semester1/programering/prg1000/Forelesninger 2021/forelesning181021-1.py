#Legge poster til fil (variabel + '\n')

nystudent = 'j'
studentfil= open('studentene.txt','a')

while nystudent == 'j':
    #Tar imot opplysniger om studenten
    studentnr=input('Oppgi studentnr: ')
    fornavn=input('Oppgi fornavn: ')
    studium=input('Oppgi studium: ')

    #Skriver studentopplysininger til  fil
    studentfil.write(studentnr+'\n')
    studentfil.write(fornavn+'\n')
    studentfil.write(studium+'\n')


    #Legge til ny student?
    nystudent = input('Vil du legge til enda en student (j/n)? ')

studentfil.close()

