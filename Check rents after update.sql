SELECT city, AVG(CAST(rent AS REAL)) AS avg_rent
FROM PropertyForRent
GROUP BY city
ORDER BY city;