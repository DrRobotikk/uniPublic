USE gruppering2022;

-- Hviser hele tabellen 
SELECT *
FROM ansatt;

-- grupperer ut med riktig måte
SELECT  Stillingskode,Lønnstrinn, COUNT(*) AS Antall
FROM ansatt
GROUP BY Stillingskode,Lønnstrinn;

SELECT Stillingskode, COUNT(*) AS AtallAnsatte
FROM ansatt
GROUP BY STILLINGSKODE;
