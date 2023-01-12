import mysql.connector

mindatabase = mysql.connector.connect(
    host='localhost', port=3306, user='Eksamenssjef', passwd='oblig2022', db='oblig2022')



hentetliste=[]
ferdigliste=[]
emneliste=[]
hentMarkor=mindatabase.cursor()

sql=('''SELECT Fornavn,Etternavn,Emne.Emnekode,Emnenavn,Dato,Karakter,Studiepoeng
FROM Emne JOIN Eksamensresultat JOIN Student
    ON (Eksamensresultat.Studentnr=Student.Studentnr)
        ON(Emne.Emnekode=Eksamensresultat.Emnekode)
WHERE Eksamensresultat.Studentnr='1000' AND Karakter IS NOT NULL
GROUP BY Fornavn,Etternavn,Emne.Emnekode,Emnenavn,Dato,Karakter,Studiepoeng 
ORDER BY RIGHT(Emne.Emnekode,4) ASC, (Emne.Emnekode)ASC, Dato ASC;   
''')

hentMarkor.execute(sql)


for row in hentMarkor:
    hentetliste+=[[row[0],row[1],row[2],row[3],row[4],row[5],row[6]]]


for n in range(len(hentetliste)):
    emneliste+=[[hentetliste[n][2],hentetliste[n][5]]]

bestekarakter=''

for m in range(len(emneliste)-1):
    if emneliste[m][0] == emneliste[m+1][0]:
        if emneliste[m][1]>=emneliste[m+1][1]:
            bestekarakter=[emneliste[m+1][1],emneliste[m+1][0]]

print(bestekarakter)



print(emneliste)
ferdigliste+=hentetliste[0][0],hentetliste[0][1]
















hentMarkor.close()






mindatabase.close()