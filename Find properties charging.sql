SELECT p.propertyNo, p.street, p.city, p.rent
FROM PropertyForRent p
WHERE p.rent > (
    SELECT AVG(p2.rent)
    FROM PropertyForRent p2
    WHERE p2.city = p.city
)
ORDER BY p.city, p.rent DESC;