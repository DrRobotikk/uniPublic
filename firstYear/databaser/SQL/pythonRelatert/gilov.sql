USE heltnydatabase;

SELECT *
FROM Vare;

DROP USER IF EXISTS 'Lagersjefen2022';
CREATE USER'Lagersjefen2022' IDENTIFIED BY 'lagerpw';

GRANT SELECT ON Vare TO 'Lagersjefen2022';

GRANT INSERT ON Vare TO 'Lagersjefen2022';

GRANT UPDATE ON Vare TO 'Lagersjefen2022';

GRANT DELETE ON Vare To 'Lagersjefen2022';

