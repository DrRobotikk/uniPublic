USE Dekkhotell;



SELECT Kunde.Mobilnr,fornavn,etternavn,Oppbevaring.regnr,Oppbevaring.innlevert,Hylle
FROM Kunde JOIN Oppbevaring
    ON Kunde.Mobilnr=Oppbevaring.Mobilnr
WHERE Utlevert