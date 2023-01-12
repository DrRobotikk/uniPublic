DROP SCHEMA IF EXISTS Egenkobling;
CREATE SCHEMA Egenkobling;
USE Egenkobling;
CREATE TABLE Ansatt (
  AnsNr SMALLINT,
  Fornavn VARCHAR(50) NOT NULL,
  Etternavn VARCHAR(50) NOT NULL,
  Adresse VARCHAR(100),
  PostNr CHAR(4) NOT NULL,
  Fødselsdato DATE,
  Kjønn CHAR(1),
  Stilling VARCHAR(50),
  årslønn DECIMAL(8, 2) NOT NULL,
  Leder SMALLINT(6),
  CONSTRAINT AnsattPN PRIMARY KEY (AnsNr),
  CONSTRAINT LederFK FOREIGN KEY(Leder) REFERENCES Ansatt(AnsNr)
);

INSERT INTO Ansatt (Leder,AnsNr, Fornavn, Etternavn, Adresse, PostNr, Fødselsdato, Kjønn, Stilling, Årslønn) VALUES
(NULL,2, 'Gunnlaug', 'Angeltveit', 'Langmyrgrenda 9', '3800', '1969-03-29', 'K', 'Markedssjef', '643200.00'),
(2,7, 'Henriette', 'Brobakken', 'Stubberud Sognsvann 1', '3800', '1971-10-01', 'K', 'Daglig leder', '833800.00'),
(2,8, 'Synøve', 'Bakketun', 'Vassøyveien 7', '3840', '1985-05-15', 'K', 'Kundebehandler', '518100.00'),
(2,1, 'Georg', 'Barth', 'Kringsjågrenda 3F', '3841', '1982-10-20', 'M', 'Lagerleder', '604900.00'),
(7,3, 'Morgan', 'Dalland', 'Jansbergveien 19', '3830', '1974-01-10', 'M', 'Innkjøper', '670500.00'),
(8,6, 'Vilde', 'Aksnes', 'Minister Ditleffs vei 44', '3810', '1977-10-11', 'K', 'Databaseadministrator', '693200.00'),
(7,9, 'Ragnvald', 'Allum', 'Utsikten 4', '3812', '1992-03-07', 'M', 'Kundebehandler', '484700.00'),
(7,11, 'Oliver', 'Abrahamsen', 'vei 3A', '3812', '1989-01-20', 'M', 'Lagermedarbeider', '466900.00'),
(8,13, 'Oda', 'Cappelen', 'Norheimskneiken 12', '3800', '1991-02-28', 'K', 'Produktutvikler', '653100.00'),
(8,16, 'Andrine', 'Ebbesen', 'Kristianias gate 9', '3800', '1988-12-27', 'K', 'Regnskapssekretær', '532300.00');


SELECT Ansatte.AnsNr,Ansatte.Etternavn,Ansatte.Fornavn,
    Lederen.Etternavn AS HarSomLeder
FROM Ansatt AS Ansatte,Ansatt AS Lederen
WHERE Ansatte.leder=lederen.AnsNr
ORDER BY HarSomLeder,Ansatte.Etternavn,Ansatte.fornavn;


SELECT*
FROM ansatt AS Ansatte INNER JOIN ansatt AS Leder ON Ansatte.AnsNr=Leder.AnsNr
ORDER BY Ansatte.Etternavn;


