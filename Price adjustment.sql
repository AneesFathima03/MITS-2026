UPDATE PropertyForRent
SET rent = CAST(rent AS REAL) * 1.05
WHERE city IN (
    SELECT city
    FROM PropertyForRent
    GROUP BY city
    HAVING AVG(CAST(rent AS REAL)) < 400
);