DROP SCHEMA IF EXISTS ansattpersonal2022;
CREATE SCHEMA ansattpersonal2022;

USE ansattpersonal2022;

CREATE TABLE Stillingstype
(
Stillingskode CHAR(4),
Stillingsbetegnelse CHAR(20),
CONSTRAINT stillingstypePK PRIMARY KEY(Stillingskode)
);

CREATE TABLE avdeling
(
Avdelingsnr CHAR(4),
Avdelingsnavn CHAR(20),
CONSTRAINT avdelingsnrPK PRIMARY KEY(avdelingsnr)
);

CREATE TABLE kurs
(
Kursnr CHAR(5),
Kursnavn CHAR(20),
CONSTRAINT KursnrPK PRIMARY KEY(Kursnr)
);

CREATE TABLE postkatalog
(
Postnr CHAR(4),
Poststed CHAR(15),
CONSTRAINT PostnrPK PRIMARY KEY(Postnr)
);

CREATE TABLE Ansatt
(
Ansattnr CHAR(4),
Fornavn CHAR(20),
Etternavn CHAR(15),
Gateadresse CHAR(20),
Telefonnr CHAR(12),
Stillingskode CHAR(4),
Avdelingsnr CHAR(4),
Postnr CHAR(4),
CONSTRAINT AnsattnrPK PRIMARY KEY(Ansattnr),
CONSTRAINT AnsattstillingstypeFK FOREIGN KEY(Stillingskode) REFERENCES Stillingstype(stillingskode),
CONSTRAINT AnsattavdelingsnrFK FOREIGN KEY(Avdelingsnr) REFERENCES Avdeling(avdelingsnr) ON DELETE SET NULL ON UPDATE CASCADE,
CONSTRAINT AnsattpostnrFK FOREIGN KEY(Postnr) REFERENCES postkatalog(Postnr) 
);

CREATE TABLE Kursdeltagelse
(
Ansattnr CHAR(4),
Kursnr CHAR(5),
Dato DATE,
Vurdering CHAR(20),
CONSTRAINT KursdeltagelsePK PRIMARY KEY(Ansattnr,Kursnr,dato),
CONSTRAINT KursdeltagelseansattnrFK FOREIGN KEY(Ansattnr) REFERENCES Ansatt(Ansattnr),
CONSTRAINT KursdeltagelsekursnrFK FOREIGN KEY(Kursnr) REFERENCES Kurs(Kursnr)
);