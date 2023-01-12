USE bysykkelordning;

Select * from sykkel;

-- OK
-- b) Lag en spørring som viser alle sykler.
SELECT * FROM sykkel
WHERE sykkelid IS NOT NULL;

-- OK
-- c) Lag en spørring som viser etternavn, fornavn og mobilnr for alle kunder, alfabetisert på etternavn.
SELECT Etternavn, Fornavn, Mobilnr 
FROM Kunde
Order BY Etternavn ASC;

-- OK
-- d) Lag en spørring som viser alle sykler som er tatt i bruk etter 1.4.2018.
SELECT * 
FROM Sykkel
WHERE Startdato> "2018-01-04";

-- OK
-- e) Lag en spørring som viser antallet kunder i By-sykkelordningen.
SELECT count(*) as AntallKunder
FROM Kunde;

-- OK
-- f) Lag en spørring som viser alle kunder og teller opp antallet utleieforhold for hver kunde. Oversikten skal også vise kunder som ennå ikke har leid sykkel.
SELECT Etternavn, Fornavn, Kunde.Mobilnr , count(Utleie.Mobilnr) AS Antall
FROM Kunde LEFT OUTER JOIN Utleie
	ON Kunde.Mobilnr = Utleie.Mobilnr
GROUP BY kunde.mobilnr;

-- OK
-- g) Lag en spørring som gir oversikt over hvilke kunder som aldri har leid en sykkel.
-- Versjon en
SELECT Etternavn, Fornavn, Kunde.Mobilnr , count(Utleie.Mobilnr) AS Antall
FROM Kunde LEFT OUTER JOIN Utleie
	ON Kunde.Mobilnr = Utleie.Mobilnr
GROUP BY kunde.mobilnr
HAVING Antall =0;
-- versjon 2
SELECT Etternavn, Fornavn, Mobilnr
FROM Kunde
WHERE Mobilnr NOT IN (SELECT Mobilnr FROM Utleie);

-- OK
-- h) Lag en spørring som viser hvilke sykler som aldri har vært utleid.
SELECT SykkelId AS SyklerAldriUtleid
FROM Sykkel
WHERE SykkelId NOT IN (SELECT SykkelId FROM Utleie);

-- OK
-- i) Lag sql-setningen for å registrere kunden (som er ny) «Tore Syklesen, +4711111111, 1111222233334444»
INSERT INTO Kunde (Mobilnr, Fornavn, Etternavn, Betalingskortnr) 
VALUES ("4711111111","Tore","Syklesen","1111222233334444");

-- OK
-- j) Lag et View som viser hvilke sykler som er tilgjengelig ved hvert sykkelstativ. Lista skal inneholde StativID, Sted og SykkelID. Kall View’et LedigeSykler.
DROP VIEW IF EXISTS LedigeSykler;
CREATE VIEW Ledigesykler ( StativID, Sted, sykkelID)AS(
select Sykkel.StativID, Sted, sykkelID
from sykkel, sykkelstativ
WHERE Sykkel.stativID = sykkelstativ.stativid);

SELECT * FROM Ledigesykler;

-- OK
-- k) Lag sql-setningen for å opprette brukeren Sykkelsjef.
DROP USER IF EXISTS 'Sykkelsjef';
CREATE USER 'Sykkelsjef';

-- OK
-- l) Lag sql-setningen for å gi brukeren Sykkelsjef lesetilgang til View’et LedigeSykler.
GRANT SELECT ON LedigeSykler TO'Sykkelsjef';

-- OK
-- m) Lag en spørring som viser alle sykler som er leid ut mer enn 100 ganger. Lista skal presenteres i synkende rekkefølge med den sykkelen med flest utleie først.
-- v1
SELECT sykkelID, count(sykkelID) AS AntallGangerLeid
FROM Kunde LEFT OUTER JOIN Utleie
	ON Kunde.Mobilnr = Utleie.Mobilnr
GROUP BY utleie.sykkelid
Having AntallGangerLeid >=3
ORDER BY AntallGangerLeid DESC;

-- v2
SELECT sykkelID,count(sykkelID) AS AntallGangerLeid from utleie
GROUP BY sykkelID
HAVING AntallGangerLeid >=3
ORDER BY AntallGangerLeid DESC;

-- Henter bare ut 10 kunder, men ellers ok
-- n) Lag en spørring som viser mobilnr, fornavn, etternavn og totalbeløpet for alle utleier for hver enkelt kunde. Lista skal presenteres i synkende rekkefølge med den kunden som har betalt mest i leie først.
SELECT Utleie.Mobilnr, Fornavn, Etternavn, SUM(Beløp) AS Totalbeløp FROM Utleie , Kunde
WHERE Utleie.Mobilnr = Kunde.Mobilnr
GROUP BY Utleie.mobilnr
ORDER BY Totalbeløp DESC;

-- OK
-- o) Lag en spørring som viser hvor mange ledige sykler som er tilgjengelig ved hvert sykkelstativ. Lista skal inneholde StativID, Sted og antall ledige sykler.
SELECT Sykkel.StativID, Sted, count(Sykkel.StativID) AS LedigeSykler
FROM sykkel, sykkelstativ
WHERE Sykkel.stativID = sykkelstativ.stativid
GROUP BY sykkelstativ.stativid;

-- OK
-- p) Lag en spørring som viser oversikt over hvilke kunder som leier en bysykkel akkurat nå. Lista skal inneholde Etternavn, Mobilnr, SykkelID, StartDato og starttidspunkt for utleien.
SELECT Etternavn,utleie.Mobilnr,Utleie.sykkelID,Utleie.Utlevert, Startdato FROM sykkel,utleie, kunde
WHERE ( sykkel.stativID IS NULL AND innlevert is NULL) AND (Utleie.Mobilnr = Kunde.mobilnr AND utleie.sykkelid = sykkel.sykkelid);

-- Henter syklene som har blitt levert tilbake på en dag i stedet for de som er over en dag, ellers OK
-- q) Lag en spørring som viser hvilke sykler, med informasjon om kunde, som ikke er levert tilbake etter ett døgn.
SELECT Etternavn,utleie.Mobilnr,Utleie.sykkelID, utlevert,innlevert  FROM sykkel,utleie, kunde
WHERE ( sykkel.stativID IS NULL) AND (Utleie.Mobilnr = Kunde.mobilnr AND utleie.sykkelid = sykkel.sykkelid) AND ((utlevert + INTERVAL 1 DAY) >= (innlevert));

-- OK
-- r) Lag en spørring som gir oversikt over den sykkelen/de syklene som har vært utleid flest ganger (flere kan altså ha «like mange og flest»).
SELECT Sykkel.SykkelID,count(Sykkel.SykkelID) AS AntallGangerLeid
FROM Sykkel, Utleie
WHERE Sykkel.sykkelid = utleie.sykkelid
GROUP BY utleie.sykkelid
HAVING AntallGangerLeid = (
	SELECT MAX(AntallGangerLeid)
	FROM (
		SELECT count(Sykkel.SykkelID) AS AntallGangerLeid
		FROM sykkel, utleie
		WHERE Sykkel.sykkelid = utleie.sykkelid
		GROUP BY  utleie.sykkelid
		 ) as tilfeldigalias
);

#current_timestamp
