USE ansattpersonal2022;

SELECT*
FROM Ansattliste
ORDER BY Etternavn;

SELECT *
FROM Ansatt INNER JOIN Postkatalog;

SELECT*
FROM Ansatt JOIN Postkatalog;

-- likkobling
SELECT Ansattnr, Fornavn, Etternavn, Gateadresse, Ansatt.Postnr, Poststed
FROM Ansatt JOIN Postkatalog
	ON Ansatt.Postnr=Postkatalog.Postnr;
    
SELECT Ansattnr, Fornavn, Etternavn, Gateadresse, Ansatt.Postnr, Poststed
FROM Ansatt JOIN Postkatalog
	USING(Postnr);
    
SELECT Etternavn, Fornavn,Stillingsbetegnelse,Avdelingsnavn
FROM Stillingstype JOIN
	(Ansatt JOIN Avdeling
		USING(Avdelingsnr))
	USING(Stillingskode);

-- ytre kobling

SELECT *
FROM Stillingstype LEFT JOIN Ansatt
	ON Stillingstype.Stillingskode=Ansatt.Stillingskode;

SELECT *
FROM Stillingstype LEFT JOIN Ansatt
	USING(Stillingskode);