import pickle 
from student import*





studentfil=open('student.dat','rb')




fortsette = True 

while fortsette == True:
    try:
        nystudent=pickle.load(studentfil)

        print(nystudent)
    
    except EOFError:
        fortsette=False