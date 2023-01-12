USE Storenuten;

INSERT INTO Kunde(Mobilnr,Fornavn,Etternavn) VALUES
('+4790734256','Robin','Tangen'),
('+4711111111','Kari','Vilikke'),
('+4722222222','Roman','Kollar'),
('+4733333333','Didrik','Sawkins'),
('+4744444444','Maria','Kata'),
('+4755555555','Vegard','Sveinsvold');


INSERT INTO Rom(Romnr,Romtype) VALUES
('1','Enkeltrom'),
('2','Enkeltrom'),
('3','Enkeltrom'),
('4','Enkeltrom'),
('5','Enkeltrom'),
('6','Dobbeltrom'),
('7','Dobbeltrom'),
('8','Dobbeltrom'),
('9','Dobbeltrom'),
('10','Dobbeltrom'),
('11','Familierom'),
('12','Familierom'),
('13','Familierom'),
('14','Familierom'),
('15','Familierom');



INSERT INTO Bestilling(Romnr,Fradato,Tildato,Mobilnr) VALUES
('1','20220407','20220410','+4790734256'),
('10','20220501','20220512','+4733333333'),
('1','20220401','20220406','+4711111111'),
('9','20220513','20220516','+4722222222'),
('15','20220416','20220422','+4790734256'),
('3','20220415','20220418','+4744444444');