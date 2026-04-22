SELECT DISTINCT clientNo, fName, lName, maxRent
FROM Client
WHERE maxRent > (
    SELECT AVG(CAST(rent AS REAL))
    FROM PropertyForRent
)
ORDER BY maxRent DESC;