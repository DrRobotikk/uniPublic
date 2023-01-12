DROP SCHEMA IF EXISTS Bysykkelordning;
CREATE SCHEMA IF NOT EXISTS Bysykkelordning;

USE bysykkelordning;

-- skal vi bytte ut alle int med CHAR/VARCHAR? (CHAR synes jeg - erik)
CREATE TABLE Sykkelstativ
(
StativID INT(3),
Sted CHAR(40),
CONSTRAINT StativIDPK PRIMARY KEY (StativID)
);


CREATE TABLE Kunde
(
Mobilnr CHAR (11),
Fornavn CHAR(30),
Etternavn CHAR (20),
Betalingskortnr CHAR(16),
CONSTRAINT MobilnrPK PRIMARY KEY (Mobilnr)
);
-- 3000 tilgjengelige sykler, 300 sykkelstativer og 6000 elektroniske låser (ca 20 pr sykkelstativ)
CREATE TABLE Lås
(
StativID INT(3),
Låsnr INT(4),
CONSTRAINT StativIDLåsnrPK PRIMARY KEY (StativID,Låsnr),
CONSTRAINT StativIDFK FOREIGN KEY (StativID) REFERENCES Sykkelstativ(StativID)
);

CREATE TABLE Sykkel
(
SykkelID INT(4),
Startdato DATE,
StativID INT(3),
Låsnr INT(4),
CONSTRAINT SykkelIDPK PRIMARY KEY (SykkelID),
CONSTRAINT SykkelLåsFK FOREIGN KEY (StativID,Låsnr) REFERENCES Lås(StativID,Låsnr)
);

CREATE TABLE Utleie
(
SykkelID INT(4),
-- utlevert må vi snakke om
Utlevert TIMESTAMP,
Mobilnr CHAR(11),
-- innlevert må vi snakke om
Innlevert TIMESTAMP NULL DEFAULT NULL,
Beløp DECIMAL(5,2),
CONSTRAINT SykkelIDUtlevertPK PRIMARY KEY (SykkelID,Utlevert),
CONSTRAINT SykkelIDFK FOREIGN KEY (SykkelID) REFERENCES Sykkel(SykkelID),
CONSTRAINT MobilnrFK FOREIGN KEY (Mobilnr) REFERENCES Kunde(Mobilnr)
);