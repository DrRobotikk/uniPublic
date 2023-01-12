-- a)

SELECT Nr, Beskrivelse
FROM hytte
WHERE ukepris<4500 and AntallSenger>=4;

-- b)
SELECT*
FROM hytte
WHERE Strøm='J' AND Dusj='J'
ORDER BY ACS(Ukepris)

-- c)
SELECT COUNT(*)
FROM hytte
ORDER BY AntallSenger

-- d)

SELECT AVG(Ukepris) as Gjennomsnittpris
FROM hytte
WHERE AntallSenger = 4;

-- e)

SELECT COUNT(*)
FROM hytte
WHERE AvsatandAlpin<500;
