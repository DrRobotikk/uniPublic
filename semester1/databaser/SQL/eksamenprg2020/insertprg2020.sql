USE BilDeling;

CREATE USER' Bilsjef' IDENTIFIED BY 'eksamen2020';

GRANT SELECT ON Kunde TO 'Bilsjef';
GRANT SELECT ON Bil TO 'Bilsjef';
GRANT SELECT ON utleie TO 'Bilsjef';



SELECT *
FROM Utleie JOIN bil
ON Utleie.Regnr=Bil.Regnr
WHERE posisjon IS NULL ;

SELECT Utleie.Regnr, Utlevert,Kunde.Mobilnr,Fornavn,Etternavn
FROM Utleie JOIN kunde
ON Utleie.Mobilnr=Kunde.Mobilnr
WHERE Innlevert IS NULL;




INSERT INTO Kunde(Mobilnr,Fornavn,Etternavn,Betalingskort) VALUES
('90734256','Robin','Tangen','11112222333'),
('11111111','Roman','Kollar','1111122222'),
('22222222','Maria','Cata','1231245345123');



INSERT INTO Bil(Regnr,Merke,Modell,Startdato,posisjon) VALUES
('LY42048','Volvo','S40','20210101','Hønegata 12'),
('LS12345','Volvo','850','20210101',NULL),
('LS54321','Volvo','940','20210101',NULL);


INSERT INTO utleie(Regnr,utlevert,KmUT,Mobilnr,Innlevert,KmINN,Beløp) VALUES
('LY42048','2022-01-03 00:00:00','2200','90734256','2022-01-04 00:00:00','2240',250),
('LS12345','2022-02-03 00:00:00','1200','11111111',NULL,NULL,NULL),
('LS54321','2022-01-03 01:00:00','1500','22222222',NULL,NULL,NULL);


