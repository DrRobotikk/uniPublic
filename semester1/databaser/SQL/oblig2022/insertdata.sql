USE oblig2022;

INSERT INTO Student(Studentnr,Fornavn,Etternavn,Epost,Telefon) VALUES
    ("1000","Robin","Tangen","tangenrobin@gmail.com","90734256"),
    ("1001","Didrik","Sawkins","sawkins@didrk.com","73821232"),
    ("1002","Erik","Bøhle","bohle@erik.com","12323456"),
    ("1003","Roman","Kollar","kollar@roman.com","98675423"),
    ("1004","Vegard","Sveinsvold","sveinsvold@vegard.com","45637256");

INSERT INTO Emne(Emnekode,Emnenavn,Studiepoeng) VALUES
("PRG1000","Grunnleggende programering 1",7.5),
("PRG1100","Grunnlegende programering 2",7.5),
("WEB1100","Webutvikling",7.5);

INSERT INTO Rom(Romnr,Antallplasser) VALUES
("E209",999),
("E215",12),
("E211",15),
("C207",5),
("E208",12),
("E123",1),
("E222",4),
("C100",1),
("C111",15);

INSERT INTO Eksamen(Emnekode,Dato,Romnr) VALUES
("PRG1000","20220307","E209"),
("PRG1100","20210616","E211"),
("WEB1100","20210312","C207"),
("PRG1100","20160405","E211"),
("PRG1000","20220412","C100"),
("PRG1000","20210616","E209");

INSERT INTO Eksamen(Emnekode,Dato,Romnr) VALUES
("PRG1100","20220525","C111");



INSERT INTO Eksamensresultat(Studentnr,Emnekode,Dato,Karakter) VALUES
("1000","PRG1000","20220307","A"),
("1001","PRG1000","20220307","B"),
("1003","WEB1100","20210312","D"),
("1004","PRG1100","20160405","F");

INSERT INTO Eksamensresultat(Studentnr,Emnekode,Dato,Karakter) VALUES
("1000","PRG1100","20220525",NULL),
("1001","PRG1100","20220525",NULL),
("1002","PRG1100","20220525",NULL),
("1003","PRG1100","20220525",NULL),
("1004","PRG1100","20220525",NULL)
;

INSERT INTO Eksamensresultat(Studentnr,Emnekode,Dato,Karakter) VALUES
("1000","WEB1100","20210312","D");

INSERT INTO Eksamensresultat(Studentnr,Emnekode,Dato,Karakter) VALUES
("1000","PRG1000","20210616","B");

INSERT INTO Eksamensresultat(Studentnr,Emnekode,Dato,Karakter) VALUES
("1003","PRG1000","20220307","A");

INSERT INTO Eksamensresultat(Studentnr,Emnekode,Dato,Karakter) VALUES
("1000","PRG1100","20160405","B");



INSERT INTO Eksamensresultat(Studentnr,Emnekode,Dato,Karakter) VALUES
("1001","WEB1100","20210312","C"),
("1002","WEB1100","20210312","C"),
("1004","WEB1100","20210312","C"),
("1005","WEB1100","20210312","C");


INSERT INTO Eksamensresultat(Studentnr,Emnekode,Dato,Karakter) VALUES
("1000","WEB1100","20220525",NULL),
("1001","WEB1100","20220525",NULL),
("1002","WEB1100","20220525",NULL),
("1003","WEB1100","20220525",NULL),
("1004","WEB1100","20220525",NULL)
;

INSERT INTO Eksamen(Emnekode,Dato,Romnr) VALUES
("WEB1100","20220525","C111");