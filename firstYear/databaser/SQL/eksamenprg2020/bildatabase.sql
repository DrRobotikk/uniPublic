DROP SCHEMA IF EXISTS BilDeling;
CREATE SCHEMA BilDeling;

USE BilDeling;

CREATE TABLE Bil(
    Regnr CHAR(7),
    Merke CHAR(15),
    Modell CHAR(15),
    Startdato DATE,
    Posisjon CHAR(30) DEFAULT NULL,
    CONSTRAINT RegnrPK PRIMARY KEY(Regnr)
);


CREATE TABLE Kunde(
    Mobilnr CHAR(11),
    Fornavn CHAR(20),
    Etternavn CHAR(20),
    Betalingskort CHAR(16),
    CONSTRAINT MobilnrPK PRIMARY KEY(Mobilnr)
);

CREATE TABLE Utleie(
    Regnr CHAR(7),
    Utlevert TIMESTAMP,
    KmUT INT(10),
    Mobilnr CHAR(11),
    Innlevert TIMESTAMP DEFAULT NULL,
    KmINN INT(10) DEFAULT NULL,
    Beløp INT(5) DEFAULT NULL,
    CONSTRAINT Regnrfk FOREIGN KEY(Regnr) REFERENCES Bil(Regnr),
    CONSTRAINT Mobilnrfk FOREIGN KEY(Mobilnr) REFERENCES Kunde(Mobilnr),
    CONSTRAINT RegnrutlevertPK PRIMARY KEY(Regnr,Utlevert)
);

