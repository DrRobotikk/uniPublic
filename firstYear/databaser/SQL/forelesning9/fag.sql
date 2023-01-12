USE Hobbyhuset;

SELECT Ordre.KNr,Fornavn,Etternavn,Adresse,Kunde.Postnr,COUNT(Ordre.KNr) AS Antallbestillinger
FROM Ordre,Kunde,Poststed
WHERE (Ordre.KNr=Kunde.KNr
    AND Kunde.Postnr=Poststed.Postnr)
GROUP BY Ordre.KNr,Fornavn,Etternavn,Adresse,Kunde.Postnr,Poststed
HAVING Antallbestillinger>=10
ORDER BY Antallbestillinger DESC;

USE Egenkobling;
SELECT*
FROM Ansatt;

SELECT Ansatte.AnsNr,Ansatte.Fornavn,Ansatte.Etternavn,Lederen.Etternavn AS HarSomLeder
FROM Ansatt AS Ansatte,Ansatt AS Lederen
WHERE Ansatte.Leder=Lederen.AnsNr
ORDER BY HarSomLeder,Ansatte.Etternavn,Ansatte.Fornavn;

SELECT Ansatte.AnsNr,Ansatte.Fornavn,Ansatte.Etternavn,Lederen.Etternavn AS HarSomLeder
FROM (Ansatt AS Ansatte) LEFT OUTER JOIN (Ansatt AS Lederen)
ON Ansatte.Leder=Lederen.AnsNr
ORDER BY HarSomLeder,Ansatte.Etternavn,Ansatte.Fornavn;

USE Hobbyhuset;
SELECT Vare1.VNr,Vare1.Betegnelse,Vare1.KatNr,Vare1.Pris
FROM Vare AS Vare1
WHERE Vare1.Pris=(SELECT MIN(Vare2.Pris)
    FROM Vare AS Vare2
        WHERE Vare1.KatNr=Vare2.KatNr);

CREATE VIEW BilligsteIKategori AS
(
    SELECT KatNr,MIN(Pris) AS Billigste
    FROM Vare
    GROUP BY KatNr
);

SELECT*
FROM BilligsteIKategori;

SELECT VNr,Betegnelse,Pris,Vare.KatNr
FROM Vare,BilligsteIKategori
WHERE Vare.KatNr=BilligsteIKategori.KatNr
    AND Vare.Pris = BilligsteIKategori.Billigste;


SELECT VNr,Betegnelse,Pris,Vare.KatNr
FROM Vare,(SELECT KatNr,MIN(Pris) AS Billigste
            FROM vare
            GROUP BY KatNr) AS BiK
WHERE Vare.KatNr=BiK.KatNr
    AND Vare.Pris=Bik.Billigste;