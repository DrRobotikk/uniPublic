USE Hobbyhuset;

SELECT Ordre.*,Fornavn,Etternavn,Poststed
FROM Ordre,Kunde,Poststed
WHERE Ordre.KNr=Kunde.KNr
	AND Kunde.Postnr=Poststed.Postnr;

SELECT Kunde.KNr,Etternavn, COUNT(*) AS AntallOrdre
FROM Kunde,Ordre
WHERE Kunde.KNr=Ordre.KNr
GROUP BY Kunde.KNr,Etternavn;

SELECT Kunde.KNr,Etternavn, COUNT(*) AS AntallOrdre
FROM Kunde,Ordre
WHERE Kunde.KNr=Ordre.KNr
GROUP BY Kunde.KNr,Etternavn
HAVING AntallOrdre>=10;

SELECT*
FROM Kunde
WHERE KNr IN (SELECT KNr FROM Ordre);

SELECT *
FROM Kunde
WHERE KNr NOT IN (SELECT KNr FROM Ordre);

CREATE VIEW GodeKunder AS(
SELECT*
FROM Kunde
WHERE KNr IN
	(SELECT KNr FROM Ordre)
);

SELECT*
FROM GodeKunder;