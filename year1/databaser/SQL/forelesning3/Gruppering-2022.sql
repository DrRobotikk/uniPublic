DROP SCHEMA IF EXISTS gruppering2022;
CREATE SCHEMA gruppering2022;

USE gruppering2022;

CREATE TABLE Ansatt
(
Ansattnr CHAR(4),
Fornavn CHAR(15) NOT NULL,
Stillingskode CHAR(4),
Lønnstrinn CHAR(2),
Avdelingsnr CHAR(4),
CONSTRAINT AnsattPK PRIMARY KEY (Ansattnr)
);

INSERT INTO Ansatt VALUES ('1','Brit','1008','66','3');
INSERT INTO Ansatt VALUES ('2','Borg','1008','66','3');
INSERT INTO Ansatt VALUES ('10','Robin','1118','99','1');
INSERT INTO Ansatt VALUES ('8','Didrik','1000','1','2');
INSERT INTO Ansatt VALUES ('7','Roman','1118','72','1');
INSERT INTO Ansatt VALUES ('3','Eirik','1008','72','2');
INSERT INTO Ansatt VALUES ('13','Marita','1118','99','1');
INSERT INTO Ansatt VALUES ('26','Maria','1008','1','2');

-- resten fyller du ut
-- flere ansatte på samme/forskjellige lønnstrinn på samme/forskjellige stillingskoder på samme/forskjellige avdelinger
