USE ansattpersonal2022;

-- Data i tabellen ansatt
SELECT*
FROM ansatt;

-- Data i tabelen postkatalog
SELECT*
FROM postkatalog;

-- Kryssproduktet av postkatalog og ansatt
SELECT *
FROM postkatalog,ansatt;

-- Likekobling, liste over ansatte med postadresser, med WHERE betigelse
SELECT*
FROM ansatt,postkatalog
WHERE ansatt.postnr=postkatalog.postnr;

-- med et kolonne utvalg
SELECT ansattnr,fornavn,etternavn,gateadresse,ansatt.postnr,poststed
FROM ansatt,postkatalog
WHERE ansatt.postnr=postkatalog.postnr;

-- Likekobling, liste over ansatte med postadresser, med INNER JOIN
SELECT ansattnr,fornavn,etternavn,gateadresse,ansatt.postnr,poststed
FROM ansatt INNER JOIN postkatalog
	ON ansatt.postnr=postkatalog.postnr;
    
-- Likekobling 3 tabeller, liste over ansatte med stilling og avdeling, med WHERE betigelse
SELECT etternavn,fornavn,stillingsbetegnelse,avdelingsnavn
FROM ansatt,stillingstype,avdeling
WHERE ansatt.stillingskode=stillingstype.stillingskode
	AND ansatt.avdelingsnr=avdeling.avdelingsnr;

-- Ved bruk av INNER JOIN 'viktig med steg for steg oppbyggning'
SELECT etternavn,fornavn,stillingsbetegnelse,avdelingsnavn
FROM stillingstype INNER JOIN
	(ansatt INNER JOIN avdeling
		ON ansatt.avdelingsnr=avdeling.avdelingsnr)
	ON stillingstype.Stillingskode=ansatt.avdelingsnr;

-- Veiw/utsnitt
DROP VIEW IF EXISTS ansattliste;
CREATE VIEW ansattliste(etternavn,fornavn,stilling,avdeling) AS
(SELECT etternavn,fornavn,stillingsbetegnelse,avdelingsnavn
FROM ansatt,stillingstype,avdeling
WHERE ansatt.stillingskode=stillingstype.Stillingskode
	AND ansatt.avdelingsnr=avdeling.avdelingsnr);
-- spørring på utsnitt
SELECT *
FROM ansattliste
ORDER BY etternavn;

-- Ytre koblinger
SELECT *
FROM stillingstype LEFT OUTER JOIN ansatt
	ON stillingstype.stillingskode=stillingstype.stillingskode;