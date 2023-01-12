
-- Oppgave 4 kapittel 5
USE Hobbyhuset;

CREATE VIEW Bestilling(VNr, Navn,Hylle,Pris) AS SELECT VNr,Betegnelse,hylle,Pris
FROM Vare
WHERE Antall<5;

SELECT*
FROM Bestilling;

SELECT*
FROM Vare;

SELECT VNr,Navn
FROM bestilling
WHERE Pris>100
ORDER BY Navn;

SELECT VNr,Betegnelse AS Navn
FROM Vare
WHERE Antall<5 AND Pris>100
ORDER BY Navn;

-- Oppg 5 Kapittel 5

CREATE VIEW AntallVarerPrKategori AS SELECT KatNr,COUNT(*) AS Antall
FROM Vare
GROUP BY KatNr;

SELECT*
FROM AntallVarerPrKategori;

SELECT*
FROM AntallVarerPrKategori
WHERE Antall >5;

SELECT  KatNr,COUNT(*) AS Antall
FROM Vare;

SELECT KatNr,COUNT(*) AS Antall
FROM Vare
GROUP BY KatNr
HAVING Antall>5;

-- Oppgave 1 kapittel 4

-- Radene = AntallVarer*AntallKategorier

-- En likekobling gjør at vi får antall rader = antall varer vi knytter sammen
SELECT*
FROM Vare,Kategori
WHERE Vare.KatNr=Kategori.KatNr;

SELECT *
FROM Ordrelinje;

SELECT*
FROM Vare;

SELECT Vare.Betegnelse,Ordrelinje.OrdreNr,Vare.VNr,PrisPrEnhet,Ordredato
FROM Ordrelinje,Vare,Ordre
WHERE Ordrelinje.VNr=Vare.VNr
    AND Ordre.OrdreNr=Ordrelinje.OrdreNr;