##Leser poster fra fil (uten og med rstrip)

studentfil=open('studentene.txt','r')

#Leser første linje/ første feilt i første post
studentnr=studentfil.readline()


while studentnr !='':
    studentnr=studentnr.rstrip('\n')
    #leser resten av posten
    #Leser inn fornavn og studium og strip i en opperasjon
    fornavn=studentfil.readline().rstrip('\n')
    studium=studentfil.readline().rstrip('\n')

    #Skriver ut posten
    print(studentnr,fornavn,studium)

    #Leser studentnr til neste student
    studentnr=studentfil.readline()

studentfil.close()