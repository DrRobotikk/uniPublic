DROP SCHEMA IF EXISTS storenuten;
CREATE SCHEMA storenuten;
USE Storenuten;
CREATE TABLE Kunde(
  Mobilnr CHAR(11),
  Fornavn CHAR(15),
  Etternavn CHAR(25),
  CONSTRAINT MobilnrPK PRIMARY KEY(Mobilnr)
);
CREATE TABLE Rom(
  Romnr CHAR(4),
  romtype CHAR(20),
  CONSTRAINT RomnrPK PRIMARY KEY(Romnr)
);
CREATE TABLE Bestilling(
  Romnr CHAR(4),
  Fradato DATE,
  Tildato DATE,
  Mobilnr CHAR(11),

  CONSTRAINT RomnrFradatoPK PRIMARY KEY(Romnr,Fradato),
  CONSTRAINT RomnrFK FOREIGN KEY(Romnr) REFERENCES Rom(Romnr),
  CONSTRAINT MobilnrFK FOREIGN KEY(Mobilnr) REFERENCES Kunde(Mobilnr)

);