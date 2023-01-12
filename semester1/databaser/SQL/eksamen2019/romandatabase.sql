DROP SCHEMA IF EXISTS DogStore;
CREATE SCHEMA DogStore;

USE DogStore;

CREATE TABLE Kunde
(
	Mobilnr CHAR(8) NOT NULL,
    Fornavn CHAR (15) NOT NULL,
    Etternavn CHAR(25) NOT NULL,
    Betalingskort CHAR(16) NOT NULL,
    CONSTRAINT KundePK PRIMARY KEY (Mobilnr)
);

CREATE TABLE Senter
(
	SenterID CHAR(4),
    Senternavn CHAR(20),
    CONSTRAINT SenterPK PRIMARY KEY (SenterID)
);

CREATE TABLE Boks
(
	BoksID CHAR(4),
    SenterID CHAR(4),
    CONSTRAINT BoksPK PRIMARY KEY (BoksID),
    CONSTRAINT BoksSenterFK FOREIGN KEY (SenterID) REFERENCES Senter(SenterID)
);

CREATE TABLE Hund
(
	HundeID CHAR(4),
    Hundenavn CHAR(15),
    Rase CHAR(20),
    Eier CHAR (8),
    Startdato DATE,
    CONSTRAINT HundPK PRIMARY KEY (HundeID),
    CONSTRAINT HundKundeFK FOREIGN KEY (Eier) REFERENCES Kunde(Mobilnr)
);

CREATE TABLE Utleie
(
	BoksID CHAR(4),
    Starttidspkt TIMESTAMP,
    HundeID CHAR(4),
    Sluttidspkt TIMESTAMP NULL DEFAULT NULL,
    Beløp DECIMAL(5,2),
    CONSTRAINT UtleiePK PRIMARY KEY (BoksID,Starttidspkt),
    CONSTRAINT UtleieHundFK FOREIGN KEY (HundeID) REFERENCES Hund(HundeID)
);

INSERT INTO Kunde VALUES
('11111111','aaa','aaaaa','1111111111111111'),
('22222222','bbb','bbbbb','2222222222222222'),
('33333333','ccc','ccccc','3333333333333333'),
('44444444','ddd','ddddd','4444444444444444'),
('55555555','eee','eeeee','5555555555555555'),
('66666666','fff','fffff','6666666666666666');

INSERT INTO Senter VALUES
('0001','Hønefoss'),
('0002','Jevnaker'),
('0003','Vikersund'),
('0004','Sundvollen'),
('0005','Vik');

INSERT INTO Boks (BoksID,SenterID) VALUES
('1000','0001'),
('2000','0003'),
('3000','0005'),
('4000','0002'),
('5000','0004');

INSERT INTO Hund (HundeID,Hundenavn,Rase,Eier,Startdato) VALUES
('1111','Bob','hund1','11111111',20170101),
('2222','Tom','hund2','11111111',20210101),
('3333','Eik','hund3','22222222',20220101),
('4444','Kai','hund4','33333333',20190101),
('5555','Mey','hund5','44444444',20200101),
('6666','Tim','hund6','55555555',20210202),
('7777','Man','hund7','55555555',20210303),
('8888','Dog','hund8','55555555',20200404);

INSERT INTO Utleie (BoksID,Starttidspkt,HundeID,Sluttidspkt,Beløp) VALUES
('1000','2019-01-01 12:20:02','1111','2019-01-01 16:19:21',345.50),
('1000','2022-07-21 19:40:29','1111','2022-07-21 22:20:23',200.00),
('2000','2022-01-01 12:00:00','2222','2022-01-02 12:00:00',900.00),
('2000','2022-01-03 12:00:00','2222','2022-01-03 14:30:00',245.00),
('3000','2022-01-03 12:00:00','3333','2022-01-03 14:45:00',260.00);