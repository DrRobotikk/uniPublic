USE hobbyhusetkap2

SELECT *
FROM vare
WHERE betegnelse LIKE '%,%g' OR betegnelse LIKE '%gr' OR betegnelse LIKE '%stk' AND NOT betegnelse LIKE '% stk';