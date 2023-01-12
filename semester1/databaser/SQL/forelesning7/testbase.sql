DROP SCHEMA IF EXISTS testdatabase;
CREATE SCHEMA testdatabase;

USE testdatabase;

CREATE TABLE datatyper
(
Postnr1 INTEGER,
Postnr2 CHAR(4),
Dato1 DATE,
Dato2 date
);

INSERT INTO datatyper VALUES(0304,'0304','2022-02-17',20220217);

SELECT*
FROM datatyper;

CREATE TABLE Telefonliste
(
Mobilnr CHAR(8) PRIMARY KEY,
Fornavn CHAR(15)
);

INSERT INTO Telefonliste VALUES('93031376','Ståle');

ALTER TABLE Telefonliste ADD COLUMN epost CHAR(30);

SELECT*
FROM Telefonliste;

UPDATE Telefonliste
SET epost='ståle.vikhagen@usn.no'
WHERE Mobilnr='93031376';

CREATE TABLE Postkatalog
(
Postnr CHAR(4) PRIMARY KEY,
Poststed CHAR(20) NOT NULL
);

ALTER TABLE Telefonliste ADD COLUMN Postnr CHAR(4);
ALTER TABLE Telefonliste ADD CONSTRAINT TelefonlistePostkatalogFK FOREIGN KEY
(Postnr) REFERENCES Postkatalog(postnr);

INSERT INTO Postkatalog VALUES('3470','Slemmestad');
INSERT INTO Postkatalog VALUES('6400','Molde');

UPDATE Telefonliste
SET Postnr='3470'
WHERE Mobilnr='93031376';

INSERT INTO Telefonliste (Mobilnr,Fornavn,Postnr) 
VALUES('99999999','Jens','6400');
