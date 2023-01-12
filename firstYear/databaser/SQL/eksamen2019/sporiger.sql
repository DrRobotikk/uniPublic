USE DogStore;

SELECT HundeID,Hundenavn,Rase
FROM Hund;



SELECT Etternavn,Fornavn,Mobilnr
FROM Kunde
ORDER BY Etternavn;


SELECT HundeID,Hundenavn,Rase
FROM Hund
WHERE startdato>20180101;

SELECT COUNT(Mobilnr) AS AntallKunder
FROM Kunde;

SELECT Etternavn,Fornavn,Count(utleie.HundeID) AS antallUtleie
FROM Kunde LEFT OUTER JOIN Hund
    ON Kunde.Mobilnr=Hund.Eier
    LEFT OUTER JOIN Utleie
    ON Hund.HundeID=Utleie.HundeID
GROUP BY Etternavn,Fornavn;



SELECT Etternavn,Fornavn,Mobilnr
FROM Kunde  JOIN Hund
    ON Kunde.Mobilnr=Hund.Eier
WHERE Hund.HundeID NOT IN (SELECT HundeID FROM Utleie)
GROUP BY Etternavn,Fornavn,Mobilnr;


SELECT BoksID 
FROM Boks
WHERE BoksID NOT IN ( SELECT BoksID FROM Utleie);


INSERT INTO Kunde(Mobilnr,Fornavn,Etternavn,Betalingskort) VALUES
("+4711111111","Tore","Hundemann","1111222233334444");

DROP VIEW IF EXISTS LedigeBokser;
CREATE VIEW LedigeBokser AS (
    SELECT boks.BoksID,SenterID
    FROM Boks
    WHERE Boks.BoksID NOT IN (SELECT BoksID FROM Utleie)

    
);

SELECT*
FROM LedigeBokser;

CREATE USER 'Hundesjef';

GRANT SELECT ON LedigeBokser TO 'Hundesjef';

SELECT Boks.BoksID,Senternavn,COUNT(Utleie.BoksID) AS antallUtleie
FROM Boks JOIN Senter 
    ON Boks.SenterID=Senter.SenterID
    JOIN Utleie
    ON Boks.BoksID=Utleie.BoksID
GROUP BY Boks.BoksID,Senternavn
HAVING AntallUtleie>=100
ORDER BY antallUtleie DESC;


SELECT Mobilnr,Fornavn,Etternavn, SUM(beløp) AS Totalbeløp
FROM Kunde LEFT OUTER JOIN Hund
    ON Kunde.Mobilnr=Hund.Eier
    LEFT OUTER JOIN Utleie
    ON Hund.HundeID=Utleie.HundeID
GROUP BY Mobilnr,Fornavn,Etternavn
ORDER BY Totalbeløp DESC;


SELECT Senter.SenterID,Senternavn, COUNT(Utleie.BoksID) AS AntallBokser
FROM Senter JOIN Boks
    ON Senter.SenterID=Boks.SenterID
    JOIN Utleie
        ON Boks.BoksID=Utleie.BoksID
GROUP BY SenterID,Senternavn;



SELECT Etternavn,Mobilnr,BoksID,Senternavn,starttidspkt
FROM Kunde JOIN Hund
    ON Kunde.Mobilnr=Hund.Eier
    Hund JOIN utleie
        USING HundeID
    Utleie JOIN Senter
    USING BoksID;







