USE ansattpersonal2022;


INSERT INTO avdeling(avdelingsnr,Avdelingsnavn) VALUES ('1000','IT');
INSERT INTO avdeling(avdelingsnr,Avdelingsnavn) VALUES ('2000','Administrasjon');
INSERT INTO avdeling(avdelingsnr,Avdelingsnavn) VALUES ('3000','Økonomi');
INSERT INTO avdeling(avdelingsnr,Avdelingsnavn) VALUES ('4000','Personal');
INSERT INTO avdeling(avdelingsnr,Avdelingsnavn) VALUES ('5000','Vedlikehold');


INSERT INTO stillingstype(Stillingskode,Stillingsbetegnelse) VALUES('1000','Avdelingssjef');
INSERT INTO stillingstype(Stillingskode,Stillingsbetegnelse) VALUES('2000','konsulent');
INSERT INTO stillingstype(Stillingskode,Stillingsbetegnelse) VALUES('3000','Økonomi medarbeider');
INSERT INTO stillingstype(Stillingskode,Stillingsbetegnelse) VALUES('4000','Sekretær');
INSERT INTO stillingstype(Stillingskode,Stillingsbetegnelse) VALUES('5000','Trainee');

INSERT INTO postkatalog(postnr,poststed) VALUES('1000','Storeby');
INSERT INTO postkatalog(postnr,poststed) VALUES('1500','Lilleby');
INSERT INTO postkatalog(postnr,poststed) VALUES('2000','Mellomby');
INSERT INTO postkatalog(postnr,poststed) VALUES('2500','Storebygd');
INSERT INTO postkatalog(postnr,poststed) VALUES('3000','Mellombygd');
INSERT INTO postkatalog(postnr,poststed) VALUES('3500','Lillebygd');

INSERT INTO kurs(kursnr,kursnavn) VALUES('1000','HMS');
INSERT INTO kurs(kursnr,kursnavn) VALUES('2000','Brannvakt');
INSERT INTO kurs(kursnr,kursnavn) VALUES('3000','Førstehjelp');
INSERT INTO kurs(kursnr,kursnavn) VALUES('4000','Sistehjelp');

INSERT INTO ansatt(Ansattnr,Fornavn,Etternavn,Gateadresse,Telefonnr,Stillingskode,Avdelingsnr,Postnr) VALUES('1000','Ole','Olsen','Adressa 2','89674523','1000','1000','3000');
INSERT INTO ansatt(Ansattnr,Fornavn,Etternavn,Gateadresse,Telefonnr,Stillingskode,Avdelingsnr,Postnr) VALUES('2000','Hans','Hansen','Adressa 3','99674523','4000','4000',1000);
INSERT INTO ansatt(Ansattnr,Fornavn,Etternavn,Gateadresse,Telefonnr,Stillingskode,Avdelingsnr,Postnr) VALUES('3000','Jens','Jensen','Adressa 4','89644523','2000','2000','1500');
INSERT INTO ansatt(Ansattnr,Fornavn,Etternavn,Gateadresse,Telefonnr,Stillingskode,Avdelingsnr,Postnr) VALUES('4000','trine','Trinesen','Adressa 5','89679823','5000','4000','2500');
INSERT INTO ansatt(Ansattnr,Fornavn,Etternavn,Gateadresse,Telefonnr,Stillingskode,Avdelingsnr,Postnr) VALUES('5000','Kari','Karisen','Adressa 1','19674523','3000','5000','3500');

INSERT INTO Kursdeltagelse(Ansattnr,Kursnr,Dato,Vurdering) VALUES('1000','1000','21.03.16','Bestått');
INSERT INTO Kursdeltagelse(Ansattnr,Kursnr,Dato,Vurdering) VALUES('1000','2000','21.03.16','ikke Bestått');
INSERT INTO Kursdeltagelse(Ansattnr,Kursnr,Dato,Vurdering) VALUES('2000','1000','21.03.16','Bestått');
INSERT INTO Kursdeltagelse(Ansattnr,Kursnr,Dato,Vurdering) VALUES('2000','2000','21.05.16','Bestått');
INSERT INTO Kursdeltagelse(Ansattnr,Kursnr,Dato,Vurdering) VALUES('3000','3000','21.02.16','ikke Bestått');
INSERT INTO Kursdeltagelse(Ansattnr,Kursnr,Dato,Vurdering) VALUES('4000','2000','21.03.17','Bestått');
INSERT INTO Kursdeltagelse(Ansattnr,Kursnr,Dato,Vurdering) VALUES('5000','2000','21.03.17','Bestått');
INSERT INTO Kursdeltagelse(Ansattnr,Kursnr,Dato,Vurdering) VALUES('5000','3000','21.03.16','Bestått');

-- oppgaver fra ståle
-- INSERT INTO Kursdeltagelse(Ansattnr,Kursnr,Dato,Vurdering) VALUES('6000','1000','21,03,17','bestått')
-- Kan ikke legge inn dette siden det ikke er riktig fremmed nøkkel til en primary key

-- INSERT INTO Kursdeltagelse VALUES('1000','6666','22.05.18','bestått')
-- Kan ikke legges til fordi fremmed nøkkel ikke er lik en primærnøkkel

