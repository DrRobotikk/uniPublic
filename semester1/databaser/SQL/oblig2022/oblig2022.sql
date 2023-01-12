DROP SCHEMA IF EXISTS oblig2022;
CREATE SCHEMA oblig2022;
USE oblig2022;
CREATE TABLE Student (
  Studentnr CHAR(6),
  Fornavn CHAR(30),
  Etternavn CHAR(20),
  Epost CHAR(40),
  
  Telefon CHAR(8),
  CONSTRAINT StudentPK PRIMARY KEY(Studentnr)
);
CREATE TABLE Emne (
  Emnekode CHAR(8),
  Emnenavn CHAR(40),
  Studiepoeng DECIMAL(3, 1),
  CONSTRAINT EmnePK PRIMARY KEY(Emnekode)
);
CREATE TABLE Rom (
  Romnr CHAR(4),
  Antallplasser INTEGER(3),
  CONSTRAINT RomPK PRIMARY KEY(Romnr)
);
CREATE Table Eksamen (
  Emnekode CHAR(8),
  Dato DATE,
  Romnr CHAR(4),
  CONSTRAINT EksamenPK PRIMARY KEY(Emnekode,Dato),
  CONSTRAINT EmnekodeFK FOREIGN KEY(Emnekode) REFERENCES Emne(Emnekode),
  CONSTRAINT RomnrFK FOREIGN KEY(Romnr) REFERENCES Rom(Romnr)
);
CREATE TABLE Eksamensresultat (
  Studentnr CHAR(6),
  Emnekode CHAR(8),
  Dato DATE,
  Karakter CHAR(1),
  CONSTRAINT EksamensresultatPK PRIMARY KEY(Studentnr, Emnekode, Dato),
  CONSTRAINT StudentnrFK FOREIGN KEY(Studentnr) REFERENCES Student(Studentnr),
  CONSTRAINT emnekodeDatoFK FOREIGN KEY(Emnekode,Dato) REFERENCES Eksamen(Emnekode,Dato)
);