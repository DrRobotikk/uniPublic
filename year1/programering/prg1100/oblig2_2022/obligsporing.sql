USE Oblig2022;

SELECT*
FROM Student;

SELECT *
FROM Eksamen;

SELECT Rom.Romnr
FROM Rom LEFT OUTER JOIN eksamen
    ON Rom.Romnr=Eksamen.Romnr
WHERE Rom.Romnr NOT IN(SELECT Romnr FROM Eksamen) AND Eksamen.Dato NOT IN (SELECT Dato FROM Eksamen) ;

SELECT Eksamen.Emnekode,Emne.Emnenavn,Emne.Studiepoeng,Eksamen.Romnr
FROM Eksamen JOIN emne
    ON Eksamen.Emnekode=Emne.Emnekode
WHERE Dato  BETWEEN '20180101' AND '20220101';

SELECT eksamensresultat.Studentnr,Emne.emnenavn,eksamensresultat.Dato,Eksamensresultat.Karakter
FROM eksamensresultat JOIN emne
    ON eksamensresultat.Emnekode=emne.Emnekode
WHERE Studentnr='1000';

SELECT Emne.Emnenavn,eksamensresultat.Dato,eksamensresultat.Karakter,COUNT(eksamensresultat.Karakter) AS Antall
FROM eksamensresultat JOIN emne
    ON eksamensresultat.Emnekode=Emne.Emnekode
WHERE Emne.Emnekode='PRG1000' 
GROUP BY Emne.Emnenavn,eksamensresultat.Dato,eksamensresultat.Karakter
ORDER BY eksamensresultat.Dato;



SELECT Emne.Emnekode,Eksamensresultat.Dato,Eksamensresultat.Karakter,Studiepoeng
FROM Emne JOIN Eksamensresultat
    ON Emne.Emnekode=Eksamensresultat.Emnekode
WHERE Studentnr='1000' AND Karakter IS NOT NULL
GROUP BY Emne.Emnenavn,Eksamensresultat.Dato,Eksamensresultat.Karakter
ORDER BY RIGHT(Emne.Emnekode,4) ;


SELECT Romnr
FROM eksamen
WHERE Emnekode='PRG100',Dato='20210616' NOT IN(SELECT Emnekode,Dato FROM Eksamen);

SELECT  Emnekode,Emnenavn, Dato,MIN(Karakter) AS Karakter
FROM Eksamensresultat 
    JOIN Emne USING (Emnekode)
    JOIN Student USING(Studentnr)
WHERE Studentnr='1000' AND Karakter IS NOT NULL
GROUP BY Emnekode,Emnenavn
ORDER BY Emnekode ASC;




SELECT Emnekode,Dato,Karakter
FROM eksamensresultat
WHERE Studentnr='1000'
GROUP BY Emnekode
HAVING Karakter LIKE(SELECT MIN(Karakter) FROM eksamensresultat);


SELECT*
FROM eksamensresultat
WHERE Studentnr='1004'



