USE Storenuten;

SELECT *
FROM Rom
ORDER BY Romnr;

SELECT *
FROM Bestilling;




DROP VIEW IF EXISTS Booket;

CREATE VIEW Booket AS(
SELECT *
FROM Rom LEFT OUTER JOIN Bestilling
    USING(Romnr)
WHERE Fradato<=20220513 OR Tildato>=20220520);



SELECT Romnr
FROM Rom
WHERE Romnr NOT IN(SELECT Romnr
    FROM Booket);



SELECT DISTINCT Romnr,Fradato,Tildato
FROM Rom LEFT OUTER JOIN Bestilling
    USING(Romnr)
GROUP BY Romnr,Fradato,TIldato
Having Fradato<=20220413 OR Tildato>=20220420;

SELECT DISTINCT Rom.Romnr
FROM Rom LEFT OUTER JOIN Bestilling
    USING(Romnr)
WHERE (Fradato<=20220513 AND Tildato<=20220513) OR (Fradato>=20220520 AND Tildato>=20220520) 
OR (Rom.Romnr NOT IN(SELECT Romnr FROM Bestilling));



DROP VIEW IF EXISTS LedigeRom;

CREATE VIEW  LedigeRom AS (
    
SELECT DISTINCT Rom.Romnr
FROM Rom LEFT OUTER JOIN Bestilling
    USING(Romnr)
WHERE (Fradato<=20220413 AND Tildato<=20220413) OR (Fradato>=20220420 AND Tildato>=20220420) 
OR (Rom.Romnr NOT IN(SELECT Romnr FROM Bestilling))

);



SELECT*
FROM LedigeRom