USE Bysykkelordning;

-- b

SELECT*
FROM Sykkel;


-- c

SELECT Etternavn,Fornavn,Mobilnr
FROM kunde
ORDER BY Etternavn;

-- d

SELECT *
FROM sykkel
WHERE Startdato>='20180401';

-- e
SELECT COUNT(*) AS AntallKunder
FROM Kunde;

-- f
SELECT Etternavn,Fornavn,Kunde.Mobilnr,COUNT(Utleie.mobilnr) AS AntallUtleie
FROM Kunde LEFT OUTER JOIN Utleie
    ON Kunde.Mobilnr=Utleie.Mobilnr
GROUP BY Etternavn,Fornavn,Kunde.Mobilnr;

-- g
SELECT Etternavn,Fornavn,Kunde.Mobilnr
FROM Kunde
WHERE Kunde.mobilnr NOT IN (SELECT Utleie.Mobilnr FROM Utleie);

-- h
SELECT*
FROM Sykkel
WHERE SykkelID NOT IN(SELECT SykkelID FROM Utleie);

-- i
INSERT INTO Kunde(Mobilnr,Fornavn,Etternavn,Betalingskortnr) VALUES
("+4711111111","Tore","Syklesen","1111222233334444");

-- j
DROP VIEW IF EXISTS LedigeSykler;
CREATE VIEW LedigeSykler AS
(
    SELECT Sykkel.StativID,Sted,SykkelID
    FROM Sykkel,Sykkelstativ
    WHERE Sykkel.StativID=Sykkelstativ.StativID
    
    
);
SELECT*
FROM LedigeSykler;


-- K
CREATE USER 'Sykkelsjefen' IDENTIFIED BY 'Sykkel';

-- l
GRANT SELECT ON LedigeSykler TO 'Sykkelsjefen';

-- m
SELECT Sykkel.SykkelID,COUNT(*) AS AntallGangerUtleid
FROM Sykkel,Utleie
WHERE Sykkel.SykkelID=Utleie.SykkelID
GROUP BY SykkelID
HAVING AntallGangerUtleid>2
ORDER BY AntallGangerUtleid DESC;

-- n
SELECT Kunde.Mobilnr,Fornavn,Etternavn, SUM(Beløp) AS TotalSum
FROM Kunde LEFT OUTER JOIN Utleie
    ON Kunde.Mobilnr=Utleie.Mobilnr
GROUP BY Kunde.Mobilnr,Fornavn,Etternavn
ORDER BY TotalSum DESC;

-- o
SELECT Sykkel.StativID,Sted,COUNT(*) AS AntallLedige
FROM Sykkel,Sykkelstativ
WHERE Sykkel.StativID=Sykkelstativ.StativID
GROUP BY Sykkel.StativID,sted;

-- p
SELECT Etternavn,Kunde.Mobilnr,Utleie.SykkelID,Utlevert AS StartDatoOGTidspunkt
FROM Kunde JOIN Utleie
    ON Kunde.Mobilnr=Utleie.Mobilnr
WHERE Utleie.Innlevert IS NULL;

-- q
SELECT SykkelID,Kunde.Mobilnr,Etternavn,Fornavn
FROM Kunde JOIN utleie
    ON Kunde.Mobilnr=utleie.Mobilnr
WHERE Utleie.SykkelID IN(SELECT SykkelID FROM Sykkel) AND TIMESTAMPDIFF(DAY,Utleie.Utlevert,Utleie.Innlevert)>1;






-- r
SELECT Sykkel.SykkelID,Startdato,COUNT(*) AS AntallGangerUtleid
FROM Sykkel JOIN Utleie
    ON Sykkel.SykkelID=Utleie.SykkelID
GROUP BY SykkelID
HAVING AntallGangerUtleid=(SELECT MAX(AntallGangerUtleid)
    FROM(SELECT Sykkel.SykkelID,Startdato,COUNT(*) AS AntallGangerUtleid
    FROM Sykkel JOIN Utleie
        ON Sykkel.SykkelID=Utleie.SykkelID
    GROUP BY SykkelID) AS kult)
;







