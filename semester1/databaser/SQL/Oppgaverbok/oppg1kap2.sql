USE oppgave1kap2

-- a)

SELECT*
FROM film
WHERE År=1988;

-- b)

SELECT Tittel
FROM film
WHERE ÅR BETWEEN 1980 AND 1989;

-- c)

SELECT*
FROM film
WHERE sjanger='Komedie' AND tid<130;

-- d)

SELECT Tittel
FROM film
WHERE sjanger='Action' OR sjanger='Western';

-- e)
SELECT DISTINCT Land
FROM film
ORDER BY Land;


-- g)

SELECT*
FROM film
WHERE Pris IS NULL;

-- h)

SELECT COUNT(*)
FROM film
WHERE Pris<=100;

-- i)

SELECT*
FROM film
WHERE Tittel LIKE '%now';


