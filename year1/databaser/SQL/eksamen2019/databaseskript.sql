DROP SCHEMA IF EXISTS Dogstore;
CREATE SCHEMA Dogstore;

USE Dogstore;

CREATE TABLE Senter(
    SenterID CHAR(4),
    Senternavn CHAR(25),
    CONSTRAINT SenteridPK PRIMARY KEY(SenterID)
);


CREATE TABLE Kunde(
    Mobilnr CHAR(11),
    Fornavn Char(20),
    Etternavn CHAR(25),
    Betalingskort Char(16),
    CONSTRAINT MobilnrPK PRIMARY KEY(Mobilnr)
);

CREATE TABLE Boks(
    BoksID CHAR(4),
    SenterID Char(4),
    CONSTRAINT BoksIDPK PRIMARY KEY(BoksID),
    CONSTRAINT SenterIDFK FOREIGN KEY(senterID) REFERENCES Senter(senterID)
);

CREATE TABLE Hund(
    HundeID CHAR(6),
    Hundenavn CHAR(20),
    Rase CHAR(15),
    Eier CHAR(11),
    Startdato DATE,
    CONSTRAINT HundeIDPK PRIMARY KEY(HundeID),
    CONSTRAINT EierFK FOREIGN KEY(Eier) REFERENCES Kunde(Mobilnr)
);

CREATE TABLE Utleie(
    BoksID CHAR(4),
    Starttidspkt TIMESTAMP UNIQUE ,
    HundeID CHAR(6),
    Slutttidspkt TIMESTAMP NULL DEFAULT NULL,
    Belop FLOAT(4),
    CONSTRAINT BoksIDstartPK PRIMARY KEY(BoksID,Starttidspkt),
    CONSTRAINT BoksIDFK FOREIGN KEY(BoksID) REFERENCES Boks(BoksID),
    CONSTRAINT HundeIDFK FOREIGN KEY(HundeID) REFERENCES Hund(HundeID)
);


INSERT INTO Senter(SenterID,Senternavn) VALUES
("10","StorSentret"),
("11","LilleSentret"),
("12","Brotovet"),
("13","Down Town"),
("14","Herkules");


INSERT INTO Kunde(Mobilnr,Fornavn,Etternavn,Betalingskort) VALUES
("+4722222222","Roman","Kollar","1111111111111111"),
("+4733333333","Robin","Tangen","1111111111111111"),
("+4744444444","Maria","Cata","1111111111111111"),
("+4755555555","Vegard","Sveinsvold","1111111111111111");




INSERT INTO  Boks(BoksID,SenterID) VALUES
("1","10"),
("2","10"),
("3","10"),
("4","10"),
("5","10"),
("6","11"),
("7","11"),
("8","11"),
("9","11"),
("10","11"),
("11","12"),
("13","12"),
("14","12"),
("15","12"),
("16","13"),
("17","13"),
("18","13"),
("19","13"),
("20","13"),
("21","14"),
("22","14"),
("23","14"),
("24","14"),
("25","14");


INSERT INTO Hund(HundeID,Hundenavn,Rase,Eier,startdato) VALUES
("100","Dolly","Finsklapphund","+4733333333",20200101),
("101","Kira","Finsklapphund","+4733333333",20210101),
("102","Kompis","Raring","+4722222222",20190101),
("103","Bjeffen","Hund","+4744444444",20210101);


-- INSERT INTO Utleie(BoksID,Stattidspkt,HundeID,Slutttidspkt,belop) VALUES
-- ("11",2018-01-01 00:00:00,"100",2018-01-02 00:00:00,14.99),
-- ("13",2018-01-01 00:00:00,"101",2018-01-02 00:00:00,14.99);