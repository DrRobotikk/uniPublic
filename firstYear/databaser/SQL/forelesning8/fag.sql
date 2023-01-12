USE Hobbyhuset;
CREATE VIEW salg AS
(
    SELECT OL.*,V.Betegnelse,K.Navn AS Kategori,O.OrdreDato,O.Knr
    FROM Ordre AS O,Ordrelinje AS OL, Vare AS V,Kategori AS K
    WHERE OL.OrdreNr=O.OrdreNr
        AND OL.VNr=V.VNr
        AND V.katNr=K.katNr
);

SELECT*
FROM Salg;

SELECT *
FROM ordrelinje;

-- Kunder uten bestillinger ved bruk av NOT EXISTS
SELECT *
FROM kunde
WHERE NOT EXISTS
    (SELECT KNr FROM Ordre
    WHERE Kunde.KNr=Ordre.KNr);

-- Kunder med bestillinger ved bruk av EXISTS
SELECT*
FROM Kunde
WHERE EXISTS
    (SELECT KNr FROM Ordre
    WHERE Kunde.KNr=Ordre.KNr);


SELECT VNr,Betegnelse,Pris
FROM Vare
WHERE Pris<(SELECT AVG(Pris) FROM Vare);

SELECT Vare1.VNr,Vare1.Betegnelse,Vare1.KatNr,Vare1.Pris
FROM Vare AS Vare1
WHERE Vare1.Pris=
    (SELECT MIN(Vare2.Pris)
    FROM Vare AS Vare2
        WHERE Vare1.KatNr=Vare2.KatNr);


