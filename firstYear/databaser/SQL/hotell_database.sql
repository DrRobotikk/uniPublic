DROP SCHEMA IF EXISTS hotell;
CREATE SCHEMA hotell;

USE hotell;

CREATE TABLE gjest
(
Fornavn CHAR(20),
Etternavn CHAR(20),
Telefonnr CHAR(12),
CONSTRAINT telefonnrPK PRIMARY KEY(Telefonnr)
);



CREATE TABLE bestilling
(
fra DATE,
til DATE,
antall CHAR(5),
Telefonnr CHAR(12),
Romnr CHAR(3),
CONSTRAINT fraPK PRIMARY KEY(fra,til,Romnr),
CONSTRAINT TelefonnrFK FOREIGN KEY(Telefonnr) REFERENCES gjest(Telefonnr)
);