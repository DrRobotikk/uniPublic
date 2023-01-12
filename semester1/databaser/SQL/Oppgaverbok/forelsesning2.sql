USE hobbyhusetkap2;

SELECT *
FROM vare;

-- varer som koster under 100kr i kategeorien bøker og keramikk

SELECT * 
FROM vare
WHERE pris<=100
	AND (kategori = 'bøker' or kategori = 'keramikk'); 
    
-- VNr betegnelser, pris og beregning av prisInkMva avrudnet med 2 desimaler og uten NULL-merke

SELECT VNr,betegnelse, pris, ROUND(pris*1.25,2) AS PrisInkMva
FROM vare; 


-- VNr, betegnelse og hyllebokstav navngitt som hylleseksjon

SELECT VNr,betegnelse, LEFT(Hylle,1) AS Hylleseksjon
FROM vare
WHERE UPPER(Hylle) IS NOT NULL;

-- varer med pris>=57 og pris<=75 med bruk av logisk opperator

SELECT*
FROM vare
WHERE Pris>=57 and pris<=75.50;

-- varer med pris>=57 og pris<=75 med bruk av BETWEEN

SELECT*
FROM vare
WHERE pris BETWEEN 57 AND 75.50;

-- varer med varenavn som begynner på M med mønstersammeligning

SELECT*
FROM vare
WHERE UPPER(BETEGNELSE) LIKE 'M%';

-- varer med varenavn som begynner på M med testing på likhet

SELECT *
FROM vare
WHERE LEFT(UPPER(BETEGNELSE),1)='M';

-- varer som inneholder marsipan i navnet

SELECT*
FROM vare 
WHERE UPPER(BETEGNELSE) LIKE '%MARSIPAN%';

-- alle varer, sortert på kategori og pris synkende

SELECT*
FROM vare
ORDER BY Kategori ASC, Pris DESC;

-- beregning av gjennomsnittspris for varer i kategorien Fiske, avrundet med 2 desimaler

SELECT ROUND(AVG(pris),2) AS Gjennomsnittfiske
FROM vare
WHERE Kategori='Fiske';

-- totalt antall varer i kategoriene blomsterfrø og blomsterløker

SELECT COUNT(*)
FROM vare
WHERE Kategori ='Blomsterfrø' OR kategori='Blomsterløker';

-- De kategoriene med flere enn 1 Antallvarer
SELECT kategori, count(*)
FROM vare
GROUP BY kategori
HAVING count(*)>1;






