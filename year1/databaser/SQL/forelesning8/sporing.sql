-- Grunnstrukturen for SELECT
-- SELECT
-- FROM
-- WHERE
-- GRUP  BY
-- HAVING
-- ORDER BY
USE hobbyhuset;
SELECT
  KNr,
  COUNT(*) AS AntallBestillinger
FROM
  Ordre
GROUP BY
  KNr
HAVING
  AntallBestillinger >= 10;
CREATE VIEW Gullklubben AS (
    SELECT
      KNr,
      COUNT(*) AS AntallBestillinger
    FROM
      Ordre
    GROUP BY
      KNr
    HAVING
      AntallBestillinger >= 10
  );
SELECT
  *
FROM
  Gullklubben;
SELECT
  Gullklubben.KNr,
  Fornavn,
  Etternavn,
  Adresse,
  Kunde.Postnr,
  Poststed,
  AntallBestillinger
FROM
  Gullklubben,
  Kunde,
  Poststed
WHERE
  Gullklubben.KNr = Kunde.KNr
  AND Kunde.Postnr = Poststed.Postnr;
CREATE VIEW Gullklubblista AS (
    SELECT
      Gullklubben.KNr,
      Fornavn,
      Etternavn,
      Adresse,
      Kunde.Postnr,
      Poststed,
      AntallBestillinger
    FROM
      Gullklubben,
      Kunde,
      Poststed
    WHERE
      Gullklubben.KNr = Kunde.KNr
      AND Kunde.Postnr = Poststed.Postnr
  );
SELECT
  *
FROM
  gullklubblista;
SELECT
  *
FROM
  gullklubblista
ORDER BY
  AntallBestillinger DESC;
SELECT
  Kunde.KNr,
  COUNT(*) AS AntallBestillinger,
  Fornavn,
  Etternavn,
  Adresse,
  kunde.Postnr,
  poststed
FROM
  Kunde,
  Ordre,
  poststed
WHERE
  Kunde.KNr = Ordre.KNr
  AND kunde.PostNr = poststed.PostNr
GROUP BY
  Kunde.KNr
HAVING
  AntallBestillinger >= 10;